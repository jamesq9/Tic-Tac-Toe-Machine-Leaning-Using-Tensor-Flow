from data.prepareData import work
import tensorflow as tf
import numpy as np
import random


train_x,train_y,test_x,test_y = None, None, None, None

## cols in test input data
cols_of_model = 9

## Nodes in hidden Layers
n_nodes_hl1 = 35
n_nodes_hl2 = 35
n_nodes_hl3 = 35

## Number of Oupts
n_classes = 9

## Train Batchs of Data 
batch_size = 1000

## Number of Iterations
hm_epochs = 5000

x = tf.placeholder('float')
y = tf.placeholder('float')

hidden_1_layer = {'f_fum':n_nodes_hl1,
                  'weight':tf.Variable(tf.random_normal([cols_of_model, n_nodes_hl1])),
                  'bias':tf.Variable(tf.random_normal([n_nodes_hl1]))}

hidden_2_layer = {'f_fum':n_nodes_hl2,
                  'weight':tf.Variable(tf.random_normal([n_nodes_hl1, n_nodes_hl2])),
                  'bias':tf.Variable(tf.random_normal([n_nodes_hl2]))}

hidden_3_layer = {'f_fum':n_nodes_hl3,
                  'weight':tf.Variable(tf.random_normal([n_nodes_hl2, n_nodes_hl3])),
                  'bias':tf.Variable(tf.random_normal([n_nodes_hl3]))}

output_layer = {'f_fum':None,
                'weight':tf.Variable(tf.random_normal([n_nodes_hl3, n_classes])),
                'bias':tf.Variable(tf.random_normal([n_classes])),}



def neural_network_model(data):

    l1 = tf.add(tf.matmul(data,hidden_1_layer['weight']), hidden_1_layer['bias'])
    l1 = tf.nn.relu(l1)

    l2 = tf.add(tf.matmul(l1,hidden_2_layer['weight']), hidden_2_layer['bias'])
    l2 = tf.nn.relu(l2)

    l3 = tf.add(tf.matmul(l2,hidden_3_layer['weight']), hidden_3_layer['bias'])
    l3 = tf.nn.relu(l3)

    output = tf.matmul(l3,output_layer['weight']) + output_layer['bias']

    return output

def train_neural_network(x):
	prediction = neural_network_model(x)
	cost = tf.reduce_mean( tf.nn.softmax_cross_entropy_with_logits(logits = prediction,labels=y) )
	#optimizer = tf.train.GradientDescentOptimizer(0.025).minimize(cost) 
	optimizer = tf.train.AdamOptimizer(learning_rate=0.004).minimize(cost)
	saver = tf.train.Saver()

	with tf.Session() as sess:
		sess.run(tf.global_variables_initializer())
		#print("\nfetchin Data...")
		train_x,train_y,test_x,test_y = work()
		#print("Data fetching got Completed",len(train_x), len(train_y), len(test_x) , len(test_y))
		print()
	    
		for epoch in range(hm_epochs):
			#print("shuffling data")			
			c = list(zip(train_x, train_y))
			random.shuffle(c)
			train_x, train_y = zip(*c)
			#print("Data Shuffle got Completed",len(train_x), len(train_y), len(test_x) , len(test_y))
			epoch_loss = 0
			i=0
			while i < len(train_x):
				start = i
				end = i+batch_size
				batch_x = np.array(train_x[start:end])
				batch_y = np.array(train_y[start:end])
				#print('shape of batch X is ' , batch_x.shape)
				_, c = sess.run([optimizer, cost], feed_dict={x: batch_x,
				                                              y: batch_y})
				epoch_loss += c
				i+=batch_size		
			if((epoch+1) % 500 == 0):
				print('Epoch', epoch+1, 'completed out of',hm_epochs,'loss:',epoch_loss)
				correct = tf.equal(tf.argmax(prediction, 1), tf.argmax(y, 1))
				accuracy = tf.reduce_mean(tf.cast(correct, 'float'))
				acc=accuracy.eval({x:test_x, y:test_y})
				print('Accuracy: ',acc*100.0,'%')
			if epoch_loss == 0: break
			#print()
		correct = tf.equal(tf.argmax(prediction, 1), tf.argmax(y, 1))
		accuracy = tf.reduce_mean(tf.cast(correct, 'float'))
		acc=accuracy.eval({x:test_x, y:test_y})
		print('Accuracy: ',acc*100.0,'%')
		save_path = saver.save(sess, "./model/model.ckpt")
		



if __name__ == "__main__":
    train_neural_network(x)

def use_neural_network(data):
    prediction = neural_network_model(x)
    saver = tf.train.Saver()
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        #saver = tf.train.import_meta_graph('./model.ckpt.meta')
        saver.restore(sess,"./model/model.ckpt")
        for i in data:
            result = (sess.run(tf.argmax(prediction.eval(feed_dict={x:[i]}),1)))
            print(result, end='')
            

