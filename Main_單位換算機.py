from PySide6.QtWidgets import QApplication,QMainWindow,QWidget
from Ui_單位換算機 import Ui_Form
from PySide6.QtGui import QRegularExpressionValidator
import pint #?單位換算模組

class MyWindow(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        #* 設定資料對應的單位
        self.length={'飛米':'fm','皮米':'pm','奈米':'nm','微米':'um','毫米':'mm','公分':'cm','公尺':'m','公里':'km','英吋':'in','英呎':'ft','英哩':'mi','光年':'ly','天文單位':'au'}
        self.weight={'飛克':'fg','皮克':'pg','奈克':'ng','微克':'ug','毫克':'mg','公克':'g','公斤':'kg','磅':'lb','盎司':'oz','公噸':'t','原子質量單位':'u'}
        self.temperature={'攝氏':'degC','華氏':'degF','開氏':'degK','克氏':'degK','蘭氏':'degR'}
        self.time={'飛秒':'fs','皮秒':'ps','奈秒':'ns','微秒':'us','毫秒':'ms','秒':'s','分':'min','時':'hr','日':'day','週':'week','年':'year','世紀':'century'}
        self.speed={'公尺/秒':'m/s','公里/小時':'km/hr','英哩/小時':'mi/hr','節':'knot','光速':'c'}
        self.strengh={'牛頓':'N','千牛頓':'kN','公斤力':'kgf','磅力':'lbf','達因':'dyn','克力':'gf','盎司力':'ozf','公噸力':'tf'}
        self.power={'瓦':'W','千瓦':'kW','馬力':'hp'}
        self.energy={'焦耳':'J','卡':'cal','英熱單位':'Btu','電子伏特':'eV'}
        self.pressure={'帕':'Pa','百帕':'hPa','巴':'bar','毫米汞柱':'mmHg','標準大氣壓':'atm'}
        self.area={'平方公里':'km^2','公頃':'ha','平方公尺':'m^2','平方公分':'cm^2','平方英哩':'mi^2','平方英呎':'ft^2','平方英吋':'in^2','公畝':'are','英畝':'acre'}
        self.volume={'立方公里':'km^3','立方公尺':'m^3','立方公分':'cm^3','立方英哩':'mi^3','立方英呎':'ft^3','立方英吋':'in^3','升':'L','毫升':'mL','加侖':'gal','夸脫':'qt','品脫':'pt'}
        self.byte={'位元組':'byte','位元':'bit','千位元組(KB)':'kbyte','兆位元組(MB)':'Mbyte','吉位元組(GB)':'Gbyte','太位元組(TB)':'Tbyte','拍位元組(PB)':'Pbyte','艾位元組(EB)':'Ebyte','千兆位元組(ZB)':'Zbyte','吉吉位元組(YB)':'Ybyte','千位元(Kb)':'kbit','兆位元(Mb)':'Mbit','吉位元(Gb)':'Gbit','太位元(Tb)':'Tbit','拍位元(Pb)':'Pbit','艾位元(Eb)':'Ebit','千兆位元(Zb)':'Zbit','吉吉位元(Yb)':'Ybit'}
        
        #* 設定資料類型
        self.dataType={'長度':self.length,'重量':self.weight,'溫度':self.temperature,'時間':self.time,'速度':self.speed,'力':self.strengh,'功率':self.power,'能量':self.energy,'壓力':self.pressure,'面積':self.area,'體積':self.volume,'資料儲存單位':self.byte}
        
        self.ureg=pint.UnitRegistry() #? pint初始化
        self.bind()
        
    def bind(self): #綁定事件
        self.dataTypeCombobox.addItems(self.dataType.keys())
        self.dataTypeCombobox.setCurrentIndex(0)
        self.unitComboBox_1.addItems(self.dataType[self.dataTypeCombobox.currentText()].keys())
        self.unitComboBox_2.addItems(self.dataType[self.dataTypeCombobox.currentText()].keys())
        self.dataTypeCombobox.currentIndexChanged.connect(self.changeDataType)
        self.InputLineEdit_1.setValidator(QRegularExpressionValidator('[-]{0,1}+[0-9]{0,}+[.]{0,1}+[0-9]{0,}'))
        self.InputLineEdit_2.setValidator(QRegularExpressionValidator('[-]{0,1}+[0-9]{0,}+[.]{0,1}+[0-9]{0,}'))
        self.InputLineEdit_1.textEdited.connect(lambda:self.OutputChange(1)) #! textEdited 函式修改文字時不會觸發
        self.InputLineEdit_2.textEdited.connect(lambda:self.OutputChange(2)) #! textChanged 函式修改文字時會觸發
        self.unitComboBox_1.currentIndexChanged.connect(lambda:self.OutputChange(1))
        self.unitComboBox_2.currentIndexChanged.connect(lambda:self.OutputChange(1))
        
    def OutputChange(self,state): #輸出結果
        self.caculate(state)
        a=self.InputLineEdit_1.text()
        b=self.InputLineEdit_2.text()
        if a!='':
            a=a+' '+self.unitComboBox_1.currentText()+' ='
        if b!='':
            b=b+' '+self.unitComboBox_2.currentText()
        self.orginalDataLabel.setText(a)
        self.transDataLabel.setText(b)
        
    def changeDataType(self,index): #改變資料類型
        self.unitComboBox_1.clear()
        self.unitComboBox_1.addItems(self.dataType[self.dataTypeCombobox.currentText()].keys())
        self.unitComboBox_2.clear()
        self.unitComboBox_2.addItems(self.dataType[self.dataTypeCombobox.currentText()].keys())
        self.unitComboBox_1.setCurrentIndex(0)
        self.unitComboBox_2.setCurrentIndex(0)
        self.OutputChange(1)
        
    def caculate(self,state): #計算
        if state==1:
            orginalData=float(self.InputLineEdit_1.text())
            unit_1=self.dataType[self.dataTypeCombobox.currentText()][self.unitComboBox_1.currentText()]
            unit_2=self.dataType[self.dataTypeCombobox.currentText()][self.unitComboBox_2.currentText()] #! 換Data Type時會報錯，因為unitComboBox沒有currentText()，但是不會影響結果
            result=self.ureg.Quantity(orginalData,unit_1).to(unit_2).magnitude
            self.InputLineEdit_2.setText(str(result))
        elif state==2:
            orginalData=float(self.InputLineEdit_2.text())
            unit_1=self.dataType[self.dataTypeCombobox.currentText()][self.unitComboBox_2.currentText()]
            unit_2=self.dataType[self.dataTypeCombobox.currentText()][self.unitComboBox_1.currentText()]
            result=self.ureg.Quantity(orginalData,unit_1).to(unit_2).magnitude
            self.InputLineEdit_1.setText(str(result))
            
            
        

if __name__=='__main__':
    app=QApplication([])
    window=MyWindow()
    window.show()
    app.exec()