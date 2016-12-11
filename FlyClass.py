import tensorflow as tf
import sys
import numpy

name = sys.argv[1]
img = tf.gfile.FastGFile(name, 'rb').read()
lbl_ = [line.rstrip() for line 
    in tf.gfile.GFile("retrained_labels.txt")]
with tf.gfile.FastGFile("retrained_graph.pb", 'rb') as f:
    grapho = tf.GraphDef()
    grapho.ParseFromString(f.read())
    _ = tf.import_graph_def(grapho, name='')
with tf.Session() as sess:
    tensor_ = sess.graph.get_tensor_by_name('final_result:0')
    predicted = sess.run(tensor_, \
            {'DecodeJpeg/contents:0': img})
    print("Predictions:")
    lblres = ""
    lblcsv = ""
    valres = ""
    valcsv = ""
    for i in range(0,len(lbl_)):
        lblres += lbl_[i]
        lblres += "          "
        lblcsv += lbl_[i]
        lblcsv += ','
    print(lblres)
    for j in range(0,len(predicted[0])):
        valres += str(predicted[0][j])
        valres += "       "
        valcsv += str(predicted[0][j])
        valcsv += ','
    print((valres))
    with open(name + 'Pred.csv', 'w') as f:
        f.write(lblcsv + '\n' + valcsv)
        f.close

