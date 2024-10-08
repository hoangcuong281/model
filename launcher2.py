from re import A
import ipywidgets as widgets
from IPython.display import display
from pyspark.ml.pipeline import PipelineModel
loaded_model = PipelineModel.load("./model/model_gbt")
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Create Spark Df").getOrCreate()

lb1 = widgets.HTML(value='Nhập số tuổi:')
lb2 = widgets.HTML(value='Chọn công việc:')
lb3 = widgets.HTML(value='Chọn tình trạng hôn nhân:')
lb4 = widgets.HTML(value='Chọn trình độ học vấn:')
lb5 = widgets.HTML(value='Chọn default:')
lb6 = widgets.HTML(value='Nhập số dư:')
lb7 = widgets.HTML(value='Chọn có nhà:')
lb8 = widgets.HTML(value='Chọn nợ:')
lb9 = widgets.HTML(value='Chọn phương thức liên lạc:')
lb10 = widgets.HTML(value='Nhập ngày:')
lb11 = widgets.HTML(value='Chọn tháng:')
lb12 = widgets.HTML(value='Nhập thời hạn:')
lb13 = widgets.HTML(value='Nhập campaign:')
lb14 = widgets.HTML(value='Nhập pdays:')
lb15 = widgets.HTML(value='Nhập số lần vay trước đó:')
lb16 = widgets.HTML(value='Chọn poutcome:')
lb17 = widgets.HTML(value='Đang đợi nhập')

lb1.layout.width = '250px'
lb2.layout.width = '250px'
lb3.layout.width = '250px'
lb4.layout.width = '250px'
lb5.layout.width = '250px'
lb6.layout.width = '250px'
lb7.layout.width = '250px'
lb8.layout.width = '250px'
lb9.layout.width = '250px'
lb10.layout.width = '250px'
lb11.layout.width = '250px'
lb12.layout.width = '250px'
lb13.layout.width = '250px'
lb14.layout.width = '250px'
lb15.layout.width = '250px'
lb16.layout.width = '250px'
lb17.layout.max_width = '100%'

age = widgets.FloatText()
job = widgets.Dropdown(options=['management', 'blue-collar', 'technician', 'management', 'admin.', 'services', 'retired', 'self-employed', 'student', 'unemployed', 'entrepreneur', 'housemaid', 'unknown'], disable = False)
marital = widgets.Dropdown(options=['married', 'single', 'divorced'], disable = False)
education = widgets.Dropdown(options=['secondary', 'tertiary', 'primary', 'unknown'], disable = False)
default = widgets.Dropdown(options=['yes', 'no'], disable = False)
balance = widgets.FloatText()
housing = widgets.Dropdown(options=['yes', 'no'], disable = False)
loan = widgets.Dropdown(options=['yes', 'no'], disable = False)
contact = widgets.Dropdown(options=['cellular', 'telephone', 'unknown'], disable = False)
day = widgets.FloatText()
month = widgets.Dropdown(options=['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep','oct', 'nov', 'dec'], disable = False)
duration = widgets.FloatText()
campaign = widgets.FloatText()
pdays = widgets.FloatText()
previous = widgets.FloatText()
poutcome = widgets.Dropdown(options=['other', 'success', 'failure', 'unknown'], disable = False)

predict_button = widgets.Button(description='Xác nhận')

age.layout.width = '200px'
job.layout.width = '200px'
marital.layout.width = '200px'
education.layout.width = '200px'
default.layout.width = '200px'
balance.layout.width = '200px'
housing.layout.width = '200px'
loan.layout.width = '200px'
contact.layout.width = '200px'
day.layout.width = '200px'
month.layout.width = '200px'
duration.layout.width = '200px'
campaign.layout.width = '200px'
pdays.layout.width = '200px'
previous.layout.width = '200px'
poutcome.layout.width = '200px'

def predict(b):
    a = age.value
    b = job.value
    c = marital.value
    d = education.value
    e = default.value
    f = balance.value
    g = housing.value
    h = loan.value
    i = contact.value
    j = day.value
    k = month.value
    l = duration.value
    m = campaign.value
    o = pdays.value
    p = previous.value
    q = poutcome.value

    newCus=spark.createDataFrame([
                {'age':a,
                 'job':b,
                'marital':c,
                'education':d,
                'default':e,
                'balance':f,
                'housing':g,
                'loan':h,
                'contact':i,
                'day':j,
                'month':k,
                'duration':l,
                'campaign':m,
                'pdays':o,
                'previous':p,
                'poutcome':q}])
    result = loaded_model.transform(newCus).select("deposit").first()[0]
    text = ""
    if result: text = "Dự đoán: Khách hàng này sẽ đầu tư"
    else: text = "Dự đoán: Khách hàng này sẽ không đầu tư"
    lb17.value = text
predict_button.on_click(predict)

display(widgets.HBox([lb1, age]))
display(widgets.HBox([lb2, job]))
display(widgets.HBox([lb3, marital]))
display(widgets.HBox([lb4, education]))
display(widgets.HBox([lb5, default]))
display(widgets.HBox([lb6, balance]))
display(widgets.HBox([lb7, housing]))
display(widgets.HBox([lb8, loan]))
display(widgets.HBox([lb9, contact]))
display(widgets.HBox([lb10, day]))
display(widgets.HBox([lb11, month]))
display(widgets.HBox([lb12, duration]))
display(widgets.HBox([lb13, campaign]))
display(widgets.HBox([lb14, pdays]))
display(widgets.HBox([lb15, previous]))
display(widgets.HBox([lb16, poutcome]))
display(widgets.HBox([predict_button]))
display(widgets.HBox([lb17]))


#  columns = ['age', 'job', 'marital', 'education', 'default', 'balance', 'housing', 'contact', 'day', 'month', 'duration', 'campaign', 'pdays', 'previous', 'poutcome']
