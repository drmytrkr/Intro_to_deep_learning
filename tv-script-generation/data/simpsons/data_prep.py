import helper 

data_dir = './test.txt'
text = helper.load_data(data_dir)
# Ignore notice, since we don't use it for analysing the data
text = text[81:]
text_sample = text[1:1000]
#print (text_sample)
text_sample = text_sample.split(' ')
vocab = sorted(set(text_sample))
#print (vocab)
print (len(vocab))
int_to_vocab = {}

int_to_vocab = { i : each for i , each in enumerate(vocab)}

	
print (int_to_vocab)


