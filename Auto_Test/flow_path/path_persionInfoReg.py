from enum import Enum


class path_personalInfoReg(Enum):
    # 实名认证路径
    txt_aut_css = '#root > div > div.content___17Zvm > div > div.main___1rkrS > div > div > div > div > h5'  # 实名认证title
    input_name_css = '#realName'  # 姓名
    input_idNum_css = '#idCard'  # 身份证号码
    input_phoneNum_css = '#idCard'  # 手机验证码
    btn_phoneNum_css = "#root > div > div.content___17Zvm > div > div.main___1rkrS > div > div > div > div > form > div:nth-child(3) > span"  # 手机验证码按钮
    file_idPicture1_css = '#idCardFace'  # 身份证正面
    file_idPicture2_css = '#idCardBack'  # 身份证反面
    btn_uplaodPicture1_css = '#root > div > div.content___17Zvm > div > div.main___1rkrS > div > div > div > div > form > div:nth-child(4) > div:nth-child(2) > div.ant-row.ant-form-item.undefined.undefined.ant-form-item-has-success > div > div.ant-form-item-control-input > div > span > div.ant-upload-list.ant-upload-list-picture-card > div > span > div > div'  # 身份证已上传
    btn_uplaodPicture2_css = '#root > div > div.content___17Zvm > div > div.main___1rkrS > div > div > div > div > form > div:nth-child(4) > div:nth-child(3) > div.ant-row.ant-form-item.undefined.undefined.ant-form-item-has-success > div > div.ant-form-item-control-input > div > span > div.ant-upload-list.ant-upload-list-picture-card > div > span > div'  # 身份证已上传
    btn_aut_css = '#root > div > div.content___17Zvm > div > div.main___1rkrS > div > div > div > div > button'  # 去认证按钮

    # 实名认证中路径
    txt_auting_css = '#root > div > div.content___17Zvm > div > div.main___1rkrS > div > div > div > div > div.statusWrap___1MekY.proccessing___28XxJ > p.text___3NufP'  # 认证中
    txt_name_css = '#root > div > div.content___17Zvm > div > div.main___1rkrS > div > div > div > div > ul > li:nth-child(1) > span.value___2qUi_'  # 显示姓名
    txt_idNum_css = '#root > div > div.content___17Zvm > div > div.main___1rkrS > div > div > div > div > ul > li:nth-child(2) > span.value___2qUi_'  # 显示身份证号
    txt_phoneNum_css = '#root > div > div.content___17Zvm > div > div.main___1rkrS > div > div > div > div > ul > li:nth-child(3) > span.value___2qUi_'  # 显示手机号

    # 认证成功画面
    txt_actSucess_css = '#root > div > div.content___17Zvm > div > div.main___1rkrS > div > div > div > div > div.statusWrap___1MekY.success___2iGw_ > p.text___3NufP'  # 显示手机号
    btn_actInfor_css = '#root > div > div.content___17Zvm > div > div.main___1rkrS > div > div > div > div > button'  # 显示手机号
