from enum import Enum


class loginOn(Enum):
    # 用户登录路径
    input_actLogin_css = '#userName'  # 用户名
    input_passLogin_css = '#password'  # 密码
    input_very_codeLogin_css = '#verifyCode'  # 验证码
    btn_login_css = '#root > div > div.content___17Zvm.contentLogin___1loWO > div > div > div > div > div > div > button'  # 登录按钮
    link_home_css = '#root > div > div.header___1E4MV > div > div.flex > div > a:nth-child(1)'  # 首页
    txt_loginSafe_css = '#root > div > div.content___17Zvm.contentLogin___1loWO > div > div > div > div > div > h6'  # 安全登录
    btn_pwdForget_css = '#root > div > div > div:nth-child(3) > div > button'  # 忘记密码按钮
    btn_pwdReg_css = '#root > div > div > div:nth-child(3) > div > button'  # 注册按钮

    # 用户注册路径
    btn_agree_css = 'body > div:nth-child(8) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-footer > button'  # 同意并继续按钮
    input_act_css = '#phoneNo'  # 账号输入
    input_pwd_css = '#password'  # 密码输入
    input_conPwd_css = '#confirmPassword'  # 密码再次输入
    btn_phoneCode_css = '#root > div > div > div > form > div.formItem___1pMa6.codeItem___BkaWc > span'  # 验证码输入按钮
    input_phoneCode_css = '#mobileCode'  # 验证码输入框
    btn_agreeReg = '#root > div > div > div > button'  # 注册按钮

    # 密码修改
    input_actForget_css = '#forget_tel'  # 账号输入
    input_codeForget_css = '#forget_code'  # 验证码
    input_phoneCodeForget_css = '#forget_code'  # 验证码
    btn_phoneCodeForget_css = '#root > div > div > div > form > div:nth-child(2) > div.ant-col.ant-form-item-control-wrapper > div > span > div > span.btnCode___16EUy'  # 验证码按钮
    btn_next_css = '#root > div > div > div > button'  # 下一步

    input_pwdForget_css = '#forget_password'  # 密码
    input_pwdConfirm_css = '#forget_confirmPassword'  # 确认密码
    btn_nextPwd_css = '#root > div > div > div > button'  # 下一步

    # 修改完成画面
    txt_changeOver_css = '#root > div > div > div:nth-child(3) > div > h6'  # 修改完成文本
    btn_loginNow_css = '#root > div > div > div:nth-child(3) > div > button'  # 立即登录按钮

    # 密码修改/前端
    href_passForget_css = '#root > div > div.content___17Zvm.contentLogin___1loWO > div > div > div > div > div > div > a:nth-child(1)'  # 忘记密码
    input_phoneNum_css = '#phoneNo'  # 手机号码
    input_veryCode_css = '#imgVerifiCode'  # 验证码
    input_phoneVeryCode_css = '#verifyCode'  # 验证码
    btn_phoneVeryCode_css = '#root > div > div > div:nth-child(3) > div > form > div:nth-child(3) > span'  # 验证码
    btn_nextPwd1_css = '#root > div > div > div:nth-child(3) > div > button'  # 下一步
    input_newPwd_css = '#password'
    input_newPwdCon_css = '#confirmPassword'
    btn_nextPwd2_css = '#root > div > div > div:nth-child(3) > div > form > button'  # 下一步
