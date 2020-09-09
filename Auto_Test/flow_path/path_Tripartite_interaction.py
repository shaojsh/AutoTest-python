from enum import Enum


class path_Tripartite_interaction(Enum):
    # 前端_授信申请
    btn_home_css = '#root > div > div.header___1E4MV > div > div.flex > div > a:nth-child(1)'  # 首页
    btn_apply_css = '#root > div > div.content___17Zvm > div.service-container___1yJSW > ul > li:nth-child(1) > div > a'  # 立即申请按钮
    btn_detail_xpath = "//*[text() = 'Auto_Test（专用）']/../../a/button"  # 查看详情按钮
    btn_rent_css = "#root > div > div.content___17Zvm > div > div > div > div > div.section___207eM.feature___Y1g27 > div.feature-main___3NXLZ > button"  # 立即借款
    input_bankNum_css = '#code'  # 银行账号
    select_province_css = '#province'  # 省份
    select_city_css = '#city'  # 省份
    input_branchBank_css = '#branchBank'  # 支行
    select_branchBank_css = '#purchase\.name'  # 采购项目名称
    btn_next1_css = '#root > div > div.content___17Zvm > div > div > div.ant-spin-nested-loading > div > div > div > section > div > button'  # 下一步1
    btn_next2_css = '#root > div > div.content___17Zvm > div > div > div.ant-spin-nested-loading > div > div > div > div > button.btn-primary'  # 下一步2
    checkBox_agree_css = '#root > div > div.content___17Zvm > div > div > div.ant-spin-nested-loading > div > div > div.form___X0S5x > div.checkbox___3vNvP.apply-checkbox___NbxFX > span'  # 同意chekcbox
    btn_submit_css = '#root > div > div.content___17Zvm > div > div > div.ant-spin-nested-loading > div > div > div.form___X0S5x > div.btn-wrap___2qpL6.footer-wrap___2Zh6N > button.btn-primary'  # 下一步按钮
    btn_back_css = '#root > div > div.content___17Zvm > div > div > div.ant-spin-nested-loading > div > div > div > button'  # 返回按钮
    btn_myMain_css = '#root > div > div.header___1E4MV > div > div.userNav___3Bzyb > a:nth-child(1)'  # 返回主页面

    # 授信审核
    btn_creditCheck_css = '#root > section > section > main > div > div > section:nth-child(2) > div.auditItem___1xnJl.credit___2T_gE > a'  # 授信带审查按钮
    btn_Check_css = '#root > section > section > main > div > div > div > div.bird_table___FZCrM > table > tbody > tr:nth-child(1) > td:nth-child(11) > span > a'  # 授信审核按钮
    btn_toCheck_css = 'body > div:nth-child(6) > div > div.ant-drawer-content-wrapper > div > div > div.ant-drawer-body > div > div:nth-child(2) > div.ant-tabs-bar.ant-tabs-top-bar > div > div > div > div > div:nth-child(1) > div:nth-child(2)'  # 授信审核
    input_checkMoney_css = 'body > div:nth-child(6) > div > div.ant-drawer-content-wrapper > div > div > div.ant-drawer-body > div > div:nth-child(2) > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.ant-spin-nested-loading > div > form > div:nth-child(1) > div:nth-child(1) > div > div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > div > div > div.ant-input-number-input-wrap > input'  # 授信额度
    input_checkMonth_css = 'body > div:nth-child(6) > div > div.ant-drawer-content-wrapper > div > div > div.ant-drawer-body > div > div:nth-child(2) > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.ant-spin-nested-loading > div > form > div:nth-child(1) > div:nth-child(2) > div > div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > div > div.ant-input-number-input-wrap > input'  # 授信月数
    input_checkRate_css = 'body > div:nth-child(6) > div > div.ant-drawer-content-wrapper > div > div > div.ant-drawer-body > div > div:nth-child(2) > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.ant-spin-nested-loading > div > form > div:nth-child(2) > div > div > div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > div > div.ant-input-number-input-wrap > input'  # 授信月数
    input_remarks_css = 'body > div:nth-child(6) > div > div.ant-drawer-content-wrapper > div > div > div.ant-drawer-body > div > div:nth-child(2) > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.ant-spin-nested-loading > div > form > div:nth-child(3) > div > div > div.ant-col.ant-col-17.ant-form-item-control-wrapper > div > span > textarea'  # 授信备注
    input_checkOK_css = 'body > div:nth-child(6) > div > div.ant-drawer-content-wrapper > div > div > div.ant-drawer-body > div > div:nth-child(2) > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.ant-spin-nested-loading > div > div > button.ant-btn.ant-btn-primary'  # 审核通过

    # 前端借款申请
    btn_loanApply_css = '#root > div > div.content___17Zvm > div > div.container___1ylnx > ul > li:nth-child(4) > a'  # 借款申请
    select_productName_css = '#root > div > div.content___17Zvm > div > div.main___1rkrS > div > div.searchBar___PNjiu > div:nth-child(1) > div > div > span.ant-select-selection-item'  # 产品名称检索框
    select_productNameList_css = 'body > div:nth-child(7) > div > div > div > div:nth-child(2) > div > div'  # 产品名称检索框List
    select_productQuery_css = '#root > div > div.content___17Zvm > div > div.main___1rkrS > div > div.searchBar___PNjiu > button'  # 查询按钮
    btn_productSubmit_css = '#root > div > div.content___17Zvm > div > div.main___1rkrS > div > div:nth-child(2) > div > div > div > div > div > div > a:nth-child(2)'  # 提交借款申请
    # 收款账户管理
    input_bankNumMan_css = '#code'  # 银行账号
    input_bankPhone_css = '#phone'  # 手机号码
    btn_veryCod_css = '#root > div > div.content___17Zvm > div > div.main___1rkrS > div > div > div > div > form > div:nth-child(5) > span'  # 手机验证码
    input_veryCod_css = '#phoneCode'
    btn_next_css = '#root > div > div.content___17Zvm > div > div.main___1rkrS > div > div > div > div > button'  # 下一步
    # 借款申请
    select_act_css = '#enterpriseBankId'  # 收款账户
    input_loanMoney_css = '#amount'  # 借款金额
    input_loanMonth_css = '#period'  # 借款期限
    select_repaymentWay_css = '#type'  # 还款方式
    input_reason_css = '#reason'  # 借款理由
    checkBox_agreeLoan_css = '#root > div > div.content___17Zvm > div > div > div > div > div > div.checkbox___3vNvP.checkbox___LaWOI > span'  # 同意checkbox
    btn_submitLoan_css = '#root > div > div.content___17Zvm > div > div > div > div > div > button'  # 提交申请

    # 银行借款审核
    btn_LoanCheck_css = '#root > section > section > main > div > div > section:nth-child(2) > div.auditItem___1xnJl.borrow___2wj7U > a'  # 借款审核链接
    btn_CheckBank_css = '#root > section > section > main > div > div > div > div.bird_table___FZCrM > table > tbody > tr > td:nth-child(13) > span > a'  # 借款列表审核链接
    btn_CheckOkReason_css = 'body > div:nth-child(8) > div > div.ant-drawer-content-wrapper > div > div > div.ant-drawer-body > div > div:nth-child(2) > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.ant-spin-nested-loading > div > div > form > div:nth-child(7) > div > div > div.ant-col.ant-col-18.ant-form-item-control-wrapper > div > span > textarea'  # 审批备注
    btn_CheckOkReasonRisk_css = 'body > div:nth-child(8) > div > div.ant-drawer-content-wrapper > div > div > div.ant-drawer-body > div > div:nth-child(2) > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.ant-spin-nested-loading > div > div > form > div:nth-child(8) > div > div > div.ant-col.ant-col-18.ant-form-item-control-wrapper > div > span > textarea'  # 审批备注(担保公司)
    btn_checkOkBank_css = 'body > div:nth-child(8) > div > div.ant-drawer-content-wrapper > div > div > div.ant-drawer-body > div > div:nth-child(2) > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.ant-spin-nested-loading > div > div > div > button.ant-btn.ant-btn-primary'  # 审核通过按钮
    btn_checkOkRiskMoney_css = 'body > div:nth-child(8) > div > div.ant-drawer-content-wrapper > div > div > div.ant-drawer-body > div > div:nth-child(2) > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.ant-spin-nested-loading > div > div > form > div:nth-child(7) > div > div > div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > div > div > div.ant-input-number-input-wrap > input'  # 担保费
    btn_contractNo_css = 'body > div:nth-child(6) > div > div.ant-drawer-content-wrapper > div > div > div.ant-drawer-body > div > div:nth-child(2) > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.ant-spin-nested-loading > div > div > form > div:nth-child(6) > div:nth-child(2) > div > div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > input'  # 借款担保合同编号
    btn_homeBackStage_css = '#root > section > div.sider___ER6Fg > aside > div > div > ul > li.ant-menu-item'
    txt_tag_css = '#root > section > section > main > div > div > div > div.bird_table___FZCrM > table > tbody > tr:nth-child(1) > td:nth-child(13) > span > a'  # 审核文本出现

    # 去缴费
    btn_goToPay_css = '#root > div > div.content___17Zvm > div > div.main___1rkrS > div > div:nth-child(2) > div > div > div > div > div > div > a'  # 去缴费按钮
    upload_payPicture_css = '#root > div > div.content___17Zvm > div > div > div > div > div > div > div > div > div > table > tbody > tr > td:nth-child(6) > span > div.ant-upload.ant-upload-select.ant-upload-select-text > span > input[type=file]'  # 费用图片
    btn_applyPay_css = '#root > div > div.content___17Zvm > div > div > div > button'  # 提交申请
    txt_applyPay_css = '#root > div > div.content___17Zvm > div > div > div > div > h6'  # 提交申请完成
    # 担保费审核
    btn_feeCheckMan_css = '#root > section > div.sider___ER6Fg > aside > div > div > ul > li:nth-child(9) > div.ant-menu-submenu-title > div > span'  # 借款管理
    btn_feeCheckOk_css = '#sMenu_0kaz00te8-0172-72744068-8a8a0018-000b\$Menu > li:nth-child(3) > a'  # 已审批借款
    btn_feeConfirm_css = '#root > section > section > main > div > div > div > div.bird_table___FZCrM > table > tbody > tr:nth-child(1) > td:nth-child(13) > span.actionDivider___1OyOD > a'  # 担保费确认
    input_feeMarks_css = 'body > div:nth-child(8) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > div > div > div > div > form > div:nth-child(7) > div > div > div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > textarea'  # 审核备注
    input_feeGetConfirm_css = 'body > div:nth-child(8) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > div > div > div > div > div:nth-child(3) > div > button:nth-child(1)'  # 确认收到按钮

    # 放款审核页面
    btn_loanReview_css = '#root > section > section > main > div > div > section:nth-child(2) > div.auditItem___1xnJl.hk___19KBM > a'  # 放款审核
    btn_loanCheck_css = '#root > section > section > main > div > div > div > div.bird_table___FZCrM > table > tbody > tr > td:nth-child(9) > span > a'  # 放款审核
    btn_calender_xpath = '/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[3]/div[1]/div[2]/form/div[4]/div/div/div[2]/div/span/span/div/i'  # 放款日期
    choose_calender_xpath = '/html/body/div[3]/div/div/div/div/div[2]'  # 放款日期输入框
    input_loanReason_xpath = '/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[3]/div[1]/div[2]/form/div[5]/div/div/div[2]/div/span/textarea'  # 审核备注
    btn_loanOk_xpath = "/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[3]/div[1]/div[2]/div/button[2]"  # 审核通过
    btn_tagLoan_xpath = '//*[@id="root"]/section/section/main/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/button[2]'  # 查询

    # 去还款
    btn_repayment_css = '#root > div > div.content___17Zvm > div > div.main___1rkrS > div > div:nth-child(2) > div > div > div > div > div > div > a:nth-child(3)'  # 去还款
    input_repayBankName_css = '#bankName'  # 还款银行
    input_repayBankNum_css = '#bankCode'  # 还款银行账户
    upload_repayPic_css = '#repaymentCertificate'  # 还款凭证
    checkBox_repayAgree_css = '#root > div > div.content___17Zvm > div > div > div > div > div > div > form > div.checkbox___3vNvP.checkbox___nJIKh > span'  # checkbox同意按钮
    btn_submitRepay_cs = '#root > div > div.content___17Zvm > div > div > div > div > div > div > form > button'  # 提交申请按钮
    txt_RepayOk_cs = '#root > div > div.content___17Zvm > div > div > div > h6'  # 还款申请提交完成
    # 银行还款审核
    btn_replayCheck_css = '#root > section > section > main > div > div > section:nth-child(2) > div.auditItem___1xnJl.send___aXr3A > a'  # 银行还款审核
    btn_replayCheckList_css = '#root > section > section > main > div > div > div > div.bird_table___FZCrM > table > tbody > tr > td:nth-child(13) > span > a'  # 银行还款审核列表
    input_replayReason_xpath = '/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[3]/div[1]/div[2]/div/form/div[10]/div/div/div[2]/div/span/textarea'  # 银行还款审核备注
    btn_replayOk_xpath = '/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[3]/div[1]/div[2]/div/div/div/button[2]'  # 银行审核通过
