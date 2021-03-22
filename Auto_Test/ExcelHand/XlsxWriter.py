# https://xlsxwriter.readthedocs.io/contents.html 使用官网

import xlrd
import xlsxwriter


# 创建 excel sheet ,并输入数据
def createExcel():
    # 创建 excel 文档
    workbook = xlsxwriter.Workbook('hello.xlsx')
    # 创建 excel sheet
    worksheet = workbook.add_worksheet('nihao')
    # 指定数据进行更新
    worksheet.write('B2', 'Hello world')

    workbook.close()


# 读取 指定excel 信息
def readExcel():
    excelName = 'chart.xlsx'
    data = xlrd.open_workbook(excelName)  # 打开fname文件
    data.sheet_names()  # 获取xls文件中所有sheet的名称
    table = data.sheet_by_index(0)  # 通过索引获取xls文件第0个sheet
    value = table.cell_value(2, 2)  # #获取第i行中第j列的值
    print(value)


# 柱状图生成
def barChart():
    workbook = xlsxwriter.Workbook('chart.xlsx')
    worksheet = workbook.add_worksheet()

    # Create a new Chart object.
    chart = workbook.add_chart({'type': 'column'})

    # Write some data to add to plot on the chart.
    data = [
        [1, 2, 3, 4, 5],
        [2, 4, 6, 8, 10],
        [3, 6, 9, 12, 15],
    ]

    worksheet.write_column('A1', data[0])
    worksheet.write_column('B1', data[1])
    worksheet.write_column('C1', data[2])

    # Configure the chart. In simplest case we add one or more data series.
    chart.add_series({'values': '=Sheet1!$A$1:$A$5'})
    chart.add_series({'values': '=Sheet1!$B$1:$B$5'})
    chart.add_series({'values': '=Sheet1!$C$1:$C$5'})

    # Insert the chart into the worksheet.
    worksheet.insert_chart('A7', chart)

    workbook.close()


if __name__ == "__main__":
    readExcel()
