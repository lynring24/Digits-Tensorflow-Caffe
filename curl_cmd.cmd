curl localhost:5000/login -c digits.cookie -XPOST -F username=et
curl localhost:5000/datasets/images/classification.json -b digits.cookie -XPOST -F folder_train=D:\MINST\train -F encoding=png -F resize_channels=1 -F resize_width=28 -F resize_height=28 -F method=folder -F dataset_name=mnist_dataset
curl localhost:5000/datasets/20180706-111701-2e5b/status
curl localhost:5000/index.json
# data set
curl localhost:5000/models/20180706-111701-2e5b.json
# direcroy 결과
C:\Digits\digits\jobs\20180706-111701-2e5b


# create model1
curl localhost:5000/models/images/classification.json -b digits.cookie -XPOST -F method=standard -F standard_networks=lenet -F train_epochs=30 -F framework=caffe -F model_name=lenet_base -F dataset=20180706-111701-2e5b
job_id = '20180706-115037-2f35'
curl localhost:5000/models/20180706-115037-2f35.json
# classificaion
curl localhost:5000/models/images/classification/classify_many.json -XPOST -F job_id=20180706-115037-2f35 -F image_list=@D:\MINST\Extraction\extracted.txt > predictions.txt


# create model2  : difference in epoches x3
curl localhost:5000/models/images/classification.json -b digits.cookie -XPOST -F method=standard -F standard_networks=lenet -F train_epochs=100 -F framework=caffe -F model_name=lenet_100 -F dataset=20180706-111701-2e5b
job_id : 20180706-142853-4f10
curl localhost:5000/models/images/classification/classify_many.json -XPOST -F job_id=20180706-142853-7f10 -F image_list=@D:\MINST\Extraction\extracted.txt > D:\Crawler\lenet_100.json

# create model3  : difference in epoches x6
curl localhost:5000/models/images/classification.json -b digits.cookie -XPOST -F method=standard -F standard_networks=lenet -F train_epochs=200 -F framework=caffe -F model_name=lenet_200 -F dataset=20180706-111701-2e5b
job_id :20180705-154809-8bc1
curl localhost:5000/models/images/classification/classify_many.json -XPOST -F job_id=20180705-154809-8bc1 -F image_list=@D:\MINST\Extraction\extracted.txt > D:\Crawler\lenet200.json

# create model4  : difference in solver type
curl localhost:5000/models/images/classification.json -b digits.cookie -XPOST -F method=standard -F standard_networks=alexnet -F train_epochs=30 -F framework=caffe -F model_name=alexnet -F dataset=20180706-111701-2e5b
job_id :

# create model3  : difference in epoches 1
curl localhost:5000/models/images/classification.json -b digits.cookie -XPOST -F method=standard -F standard_networks=lenet -F train_epochs=1 -F framework=caffe -F model_name=lenet_1 -F dataset=20180706-111701-2e5b
job_id : 20180706-170647-78f1
curl localhost:5000/models/images/classification/classify_many.json -XPOST -F job_id=20180706-170647-78f1 -F image_list=@D:\MINST\Extraction\extracted.txt > D:\Crawler\lenet_1.txt

20180706-173832-c600
curl localhost:5000/models/images/classification/classify_many.json -XPOST -F job_id=20180706-173832-c600 -F image_list=@D:\MINST\Extraction\extracted.txt > D:\Crawler\lenet_1_adadelta.txt