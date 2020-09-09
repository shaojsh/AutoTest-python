from enum import Enum


class path_backStage_authentication(Enum):
    # 后台认证页面
    btn_jurisdiction_xpath = "//*[text() ='权限管理']"  # 权限管理
    btn_mechanism_xpath = "//*[text() = '机构管理']"  # 机构管理
    btn_addMechanism_css = '#root > section > section > main > div > div > div > div.bird_header___1Vckx > div:nth-child(2) > div:nth-child(2) > div.ant-col.ant-col-14 > div > div > button:nth-child(1)'  # 新增按钮
    input_MechanismName_css = 'body > div:nth-child(6) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > form > div:nth-child(1) > div > div > div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > input'  # 机构名称
    input_MechanismSimName_css = 'body > div:nth-child(6) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > form > div:nth-child(2) > div > div > div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > input'  # 简称
    select_MechanismType_css = 'body > div:nth-child(6) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > form > div:nth-child(3) > div > div > div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > div > div > div'  # 机构类型
    select_BankType_xpath = "/html/body/div[3]/div/div//*[text() = '银行']"  # 机构类型:银行
    select_RiskType_xpath = "/html/body/div[3]/div/div//*[text() = '担保公司']"  # 机构类型:担保公司
    select_MechanismStatue_css = 'body > div:nth-child(6) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > form > div:nth-child(4) > div > div > div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > div > div > div'  # 机构状态
    select_StatueType_xpath = "/html/body/div[4]/div/div//*[text() = '启用']"  # 启用
    btn_confirm_css = 'body > div:nth-child(6) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > div > button'  # 确认按钮

    # 创建账号
    input_ActName_css = '#root > section > section > main > div > div > div > div > form > div:nth-child(1) > div:nth-child(1) > div > div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > input'  # 姓名
    input_PhoneNum_css = '#root > section > section > main > div > div > div > div > form > div:nth-child(1) > div:nth-child(2) > div > div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > input'  # 电话号码
    input_Email_css = '#root > section > section > main > div > div > div > div > form > div:nth-child(2) > div:nth-child(1) > div > div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > input'  # EMAIL
    input_Id_Card_css = '#root > section > section > main > div > div > div > div > form > div:nth-child(2) > div:nth-child(2) > div > div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > input'
    btn_ActConfirm_css = '#root > section > section > main > div > div > div > div > div > div > button.ant-btn.ant-btn-primary'  # 保存账户按钮

    # 修改密码
    btn_forPass_css = '#root > div > div.main___3sFq0 > div > form > div.miss___38gVa > a'  # 忘记密码

    # 认证
    txt_title_css = '#root > section > section > main > div > div > div > div > div > h5'  # 手机验证码
    input_codeAu_css = '#certificate_verifyCode'  # 手机验证码
    btn_codeAu_css = '#root > section > section > main > div > div > div > div > div > form > div:nth-child(3) > span'  # 获取验证码按钮
    upload_pic1_css = '#root > section > section > main > div > div > div > div > div > form > div:nth-child(4) > div:nth-child(2) > div > div > span > div > span > div.ant-upload.ant-upload-select.ant-upload-select-picture-card > span > input[type=file]'  # 图片1
    upload_pic2_css = '#root > section > section > main > div > div > div > div > div > form > div:nth-child(4) > div:nth-child(3) > div > div > span > div > span > div.ant-upload.ant-upload-select.ant-upload-select-picture-card > span > input[type=file]'  # 图片2
    btn_submitAu_css = '#root > section > section > main > div > div > div > div > div > form > button'  # 保存按钮

    # 企业信息认证
    input_soCode_css = '#root > section > section > main > div > div > div > div > div > form > div:nth-child(3) > div > div > div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > input'  # 社会信用代码
    input_layName_css = '#root > section > section > main > div > div > div > div > div > form > div:nth-child(4) > div > div > div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > input'  # 法人姓名
    input_IdCardLay_css = '#root > section > section > main > div > div > div > div > div > form > div:nth-child(5) > div > div > div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > input'  # 法人身份证号
    input_addressLay_css = '#root > section > section > main > div > div > div > div > div > form > div:nth-child(6) > div > div > div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > textarea'  # 法人地址
    input_postLay_css = '#root > section > section > main > div > div > div > div > div > form > div:nth-child(7) > div > div > div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > input'  # 邮政编号
    upload_pic3_css = '#root > section > section > main > div > div > div > div > div > form > div:nth-child(8) > div > div > div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > div > span > div.ant-upload.ant-upload-select.ant-upload-select-picture > span > input[type=file]'  # 上传代理委托书
    btn_goToAu_css = '#root > section > section > main > div > div > div > div > div > button'  # 去认证
    checkBox_agree_css = '#root > section > section > main > div > div > div > div > div > div.footer___-cwPP > div > label'  # 同意按钮
    btn_startAu_css = '#root > section > section > main > div > div > div > div > div > div.footer___-cwPP > button'  # 开始认证

    # 二维码认证页面
    text_au_css = '#root > section > section > main > div > div > div.statusWrap___1PwQP.success___1mF-h > p.text___9dO6n'  # 认证成功

    # 银行创建产品
    btn_goodMan_css = '#root > section > div.sider___ER6Fg > aside > div > div > ul > li.ant-menu-submenu.ant-menu-submenu-inline.ant-menu-submenu-selected > div > div > span'  # 产品管理
    btn_goodList_css = '#sMenu_0kaz0g8xh-0172-72744068-8a8a0018-0013\$Menu > li > a > span'  # 产品列表
    btn_goodAdd_css = '#root > section > section > main > div > div > div > div.bird_header___1Vckx > div:nth-child(2) > div:nth-child(2) > div.ant-col.ant-col-14 > div > div > button:nth-child(1)'  # 新增按钮
    choose_goodType_css = '#root > section > section > main > div > div:nth-child(2) > form > div:nth-child(1) > div:nth-child(1) > div > div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > div > div > div'  # 产品类型
    input_goodName_css = '#root > section > section > main > div > div:nth-child(2) > form > div:nth-child(1) > div:nth-child(2) > div > div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > input'  # 产品名称
    input_cal_css = 'body > div:nth-child(10) > div > div > div > div > div.ant-calendar-date-panel'  # 日历画布
    cal_okTime = '#root > section > section > main > div > div:nth-child(2) > form > div:nth-child(2) > div:nth-child(1) > div > div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > span > div > input'  # 生效日期
    choose_goodStatus_css = '#root > section > section > main > div > div:nth-child(2) > form > div:nth-child(2) > div:nth-child(2) > div > div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > div > div > div'  # 产品状态
    input_loanMin_css = '#root > section > section > main > div > div:nth-child(2) > form > div:nth-child(2) > div:nth-child(3) > div > div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > div > div > div.ant-input-number-input-wrap > input'  # 最小贷款
    input_loanMax_css = '#root > section > section > main > div > div:nth-child(2) > form > div:nth-child(3) > div:nth-child(1) > div > div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > div > div > div.ant-input-number-input-wrap > input'  # 最大贷款
    choose_loanGetWay_css = '#root > section > section > main > div > div:nth-child(2) > form > div:nth-child(3) > div:nth-child(2) > div > div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > div > div > div'  # 担保费收取方式
    choose_rendItem_css = '#root > section > section > main > div > div:nth-child(2) > form > div:nth-child(3) > div:nth-child(3) > div > div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > div > div > div'  # 计息单位
    choose_rendDay_css = '#root > section > section > main > div > div:nth-child(2) > form > div:nth-child(4) > div:nth-child(1) > div > div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > div > div > div'  # 计息天数
    choose_rendWay_css = '#root > section > section > main > div > div:nth-child(2) > form > div:nth-child(4) > div:nth-child(2) > div > div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > div > div > div'  # 计息规则
    input_productMon_css = '#root > section > section > main > div > div:nth-child(2) > form > div:nth-child(4) > div:nth-child(3) > div > div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > div > div.ant-input-number-input-wrap > input'  # 产品月数
    choose_giveMoneyWay_css = '#root > section > section > main > div > div:nth-child(2) > form > div:nth-child(5) > div:nth-child(1) > div > div.ant-col.ant-col-14.ant-form-item-control-wrapper > div'  # 还款方式
    input_presentYearMin_css = '#root > section > section > main > div > div:nth-child(2) > form > div:nth-child(5) > div:nth-child(2) > div > div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > div > div.ant-input-number-input-wrap > input'  # 最小年利率
    input_presentYearMax_css = '#root > section > section > main > div > div:nth-child(2) > form > div:nth-child(5) > div:nth-child(3) > div > div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > div > div.ant-input-number-input-wrap > input'  # 最大年利率
    upload_pic4_css = '#root > section > section > main > div > div:nth-child(2) > form > div:nth-child(6) > div:nth-child(1) > div > div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > div > span > div.ant-upload.ant-upload-select.ant-upload-select-picture > span > input[type=file]'  # 产品图片
    upload_pic5_css = '#root > section > section > main > div > div:nth-child(2) > form > div:nth-child(6) > div:nth-child(2) > div > div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > div > span > div.ant-upload.ant-upload-select.ant-upload-select-picture > span > input[type=file]'  # 业务申请流程图
    choose_risk_css = '#root > section > section > main > div > div:nth-child(2) > form > div:nth-child(6) > div:nth-child(3) > div > div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > div > div > div'  # 担保方
    input_area_css = '#root > section > section > main > div > div:nth-child(2) > form > div:nth-child(7) > div > div > div.ant-col.ant-col-18.ant-form-item-control-wrapper > div > span > textarea'  # 产品简介
    btn_next1_css = '#root > section > section > main > div > div:nth-child(2) > div > div > button'  # 下一步

