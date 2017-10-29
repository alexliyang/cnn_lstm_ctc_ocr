# cnn_lstm_ctc_ocr
ocr based on chinese character recognition using Convolutional Neural and lstm Networks
<br/>
### Requirement
1. tensorflow1.1.0 : window10 OS
2. Cuda (if use nvidia gpu)
3. python3.5

### Network structure
ocr is using (conv3*3*1*32——conv3*3*1*64——maxpool2*2——conv3*3*1*128——conv3*3*1*256——maxpool2*2——conv3*3*1*1——lstm*2——ctc)
![OCR-NET.png](https://github.com/zhangcheng007/cnn_lstm_ctc_ocr/blob/master/OCR-NET.png)
<br/>


### License
This code is distributed under MIT LICENSE


### References
https://github.com/ilovin/lstm_ctc_ocr<br/>