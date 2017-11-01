# cnn_lstm_ctc_ocr
ocr based on chinese character recognition using Convolutional Neural and lstm Networks
<br/>
### Requirement
1. tensorflow1.1.0 : window10 OS
2. Cuda (if use nvidia gpu)
3. python3.5
<br/>

### Network Structure
ocr is using (conv3*3*1*32——conv3*3*1*64——maxpool2*2——conv3*3*1*128——conv3*3*1*256——maxpool2*2——conv3*3*1*1——lstm*2——ctc)
<br/>
![OCR-NET.png](https://github.com/zhangcheng007/cnn_lstm_ctc_ocr/blob/master/OCR-NET.png)
<br/>
### Recognition Character 
![address.png](https://github.com/zhangcheng007/cnn_lstm_ctc_ocr/blob/master/address.png)
### License
This code is distributed under MIT LICENSE
### References
https://github.com/ilovin/lstm_ctc_ocr<br/>
https://github.com/arunpatala/captcha<br/>
https://github.com/arunpatala/reddit.captcha<br/>
https://github.com/bgeetika/Captcha-Decoder<br/>