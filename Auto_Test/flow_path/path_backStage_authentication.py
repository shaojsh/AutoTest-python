from enum import Enum


class path_backStage_authentication(Enum):
    # 后台认证页面
    btn_jurisdiction_xpath = "//*[text() ='权限管理']"  # 权限管理
    btn_mechanism_xpath = "//*[text() = '机构管理']"  # 机构管理
    btn_addMechanism_css = '#root > section > section > main > div > div > div > div.bird_header___1Vckx > div:nth-child(2) > div:nth-child(2) > div.ant-col.ant-col-14 > div > div > button:nth-child(1)'  # 新增按钮
    input_MechanismName_css = 'body > div:nth-child(6) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-body > form > div:nth-child(1) > div > div > div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > input'  # 机构名称
    input_MechanismSimName_css = 'body > div:nth-child(6) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-body > form > div:nth-child(2) > div > div > div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > input'  # 简称
    select_MechanismType_css = 'body > div:nth-child(6) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-body > form > div:nth-child(3) > div > div > div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > div > div > div'  # 机构类型
    select_MechanismStatue_css = 'body > div:nth-child(7) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-body > form > div:nth-child(4) > div > div > div.ant-col.ant-col-14.ant-form-item-control-wrapper > div > span > div > div > div'  # 确认按钮
    btn_confirm_css = 'body > div:nth-child(6) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-footer > div > button.ant-btn.ant-btn-primary'
