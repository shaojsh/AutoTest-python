from enum import Enum


class path_businessInfoReg(Enum):
    # 企业基本资料画面路径

    # 企业证件
    txt_aut_css = '#root > div > div.content___17Zvm > div > div.main___1rkrS > div > div > div > div > div > h5'  # 企业基本资料
    input_companyName_css = '#name'  # 企业名称
    display_name_xpath = '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/span/em'  # 企业名字显示
    input_companyCode_css = '#socialUniformCode'  # 社会信用代码（注册号）
    input_legalPersonName_css = '#legalName'  # 法人姓名
    input_legalPersonCardNo_css = '#idCardNo'  # 法人身份证号
    input_legalPersonAddress_css = '#address'  # 联系地址
    input_legalPersonPostCode_css = '#postCode'  # 邮政编码
    input_legalPersonIndustry_css = '#industry'  # 所属行业
    upload_legalPersonCertificate_css = '#businessCertificate'  # 营业执照
    upload_legalPersonBankNo_css = '#bankNo'  # 银行卡号
    sel_bankName_css = '#root > div > div.content___17Zvm > div > div.main___1rkrS > div > div > div > div > div > form > section:nth-child(1) > div > div:nth-child(10) > div > div > div > div > div > div > div > span.ant-select-selection-item'  # 银行卡号

    # 法定代表人证件
    sel_country_css = '#root > div > div.content___17Zvm > div > div.main___1rkrS > div > div > div > div > div > form > section:nth-child(2) > div > div:nth-child(1) > div > div > div > div > div > div > div > span.ant-select-selection-item'  # 法定代表人归属地
    sel_idCard1_css = '#legalCardFront'  # 身份证信息正面
    sel_idCard2_css = '#legalCardReverse'  # 身份证信息反面

    # 实际控制人信息
    radio_controlPerson_css = '#fillerType > label:nth-child(1) > span.ant-radio > input'  # 法定代表人radio
    upload_controlPersonId1_css = '#fillerCardFront'  # 实际控制人身份证正面
    upload_controlPersonId2_css = '#fillerCardReverse'  # 实际控制人身份证反面
    upload_controlPersonFamPic_css = '#fillerHouseholdRegister'  # 户口本页面
    radio_legalPerson_css = '#identity > label:nth-child(1) > span.ant-radio > input'  # 法定代表人radio
    bth_submit_css = '#root > div > div.content___17Zvm > div > div.main___1rkrS > div > div > div > div > div > button'  # 去认证按钮

    # 协议内容确认画面
    text_atCof_css = '#root > div > div.content___17Zvm > div > div.main___1rkrS > div > div > div > h6'  # 法定代表人radio
    checkBox_agree_xpath = '//*[@id="root"]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/span'  # checkbox
    btn_Certification_css = '#root > div > div.content___17Zvm > div > div.main___1rkrS > div > div > div > div.footer___1JfX0 > button'  # 开始认证按钮

    # 企业认证中画面
    text_atMid_css = '#root > div > div.content___17Zvm > div > div.main___1rkrS > div > div > div > div > div.statusWrap___M2YkD.proccessing___1nDUf > p.text___1dNQm'  # 企业认证中文本
    text_bank_css = '#root > div > div.content___17Zvm > div > div.main___1rkrS > div > div > div > div.bankWrap___2XSON > h6'  # 打款银行文本
    input_moneyNum_css = '#root > div > div.content___17Zvm > div > div.main___1rkrS > div > div > div > div.bankWrap___2XSON > div:nth-child(3) > div:nth-child(2) > span.input___gjIa9.ant-input-affix-wrapper > input'  # 打款银行
    btn_middleCnf_css = '#root > div > div.content___17Zvm > div > div.main___1rkrS > div > div > div > div.bankWrap___2XSON > button'  # 确认提交按钮

    # 审核中画面
    txt_examine_css = '#root > div > div.content___17Zvm > div > div.main___1rkrS > div > div > div > div > div.statusWrap___M2YkD.success___37oH- > p.text___1dNQm'  # 审核中文本
    btn_primary_css = '#root > div > div.content___17Zvm > div > div.main___1rkrS > div > div > div > div > button'  # 查看认证信息文本
