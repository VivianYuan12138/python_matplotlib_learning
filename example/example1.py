# ① 导入库
import matplotlib.pyplot as plt #导入matplotlib库中的pyplot子库
# ② 新建绘图区
fig, ax = plt.subplots(figsize=(6,4)) #指定绘图区大小为6*4英寸
plt.rcParams['font.sans-serif'] = ['SimHei'] #设置显示中文字体（黑体）
# ③ 准备数据
seazons=['一季度', '二季度', '三季度','四季度'] #设置分类轴显示文本
sales=[2780,1950,2680,2120] #设置某产品的销售量数据
index=[0,1,2,3] #index控制分类轴刻度
barW=0.7 #barW控制条形的宽度
# ④ 设置图表属性
plt.title("产品销售") #设置图表标题
plt.xlabel("时间") #设置X坐标轴标签
plt.ylabel("销售量") #设置Y坐标轴标签
plt.xticks(index,seazons) #设置分类轴标记
plt.grid(axis="y") #显示横向网格线
# ⑤ 绘制图表
plt.bar(index,sales,barW,color='b',label='某产品') #绘制柱状图
for a,b in zip(index,sales): #显示数值标注
    plt.text(a,b+30, '%.0f'%b, ha='center', fontsize=9) #ha设置水平对齐方式
# ⑥ 显示图例
plt.legend(loc='upper right' ) #在右上角显示图例文字
# ⑦ 显示图表
plt.show( )