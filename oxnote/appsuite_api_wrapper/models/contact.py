#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
from typing import List

from appsuite_api_wrapper.models.appsuite_id_model import IdAttributeMap, AppsuiteIdModel
from appsuite_api_wrapper.models.distribution_list_member import DistributionListMember

logger = logging.getLogger(__name__)


class ContactAttributeMap(IdAttributeMap):
    uid = 'uid'
    display_name = 'display_name'
    first_name = 'first_name'
    last_name = 'last_name'
    second_name = 'second_name'
    suffix = 'suffix'
    title = 'title'
    street_home = 'street_home'
    postal_code_home = 'postal_code_home'
    city_home = 'city_home'
    state_home = 'state_home'
    country_home = 'country_home'
    birthday = 'birthday'
    marital_status = 'marital_status'
    number_of_children = 'number_of_children'
    profession = 'profession'
    nickname = 'nickname'
    spouse_name = 'spouse_name'
    anniversary = 'anniversary'
    note = 'note'
    department = 'department'
    position = 'position'
    employee_type = 'employee_type'
    room_number = 'room_number'
    street_business = 'street_business'
    postal_code_business = 'postal_code_business'
    city_business = 'city_business'
    state_business = 'state_business'
    country_business = 'country_business'
    user_id = 'user_id'
    number_of_employees = 'number_of_employees'
    sales_volume = 'sales_volume'
    tax_id = 'tax_id'
    commercial_register = 'commercial_register'
    branches = 'branches'
    business_category = 'business_category'
    info = 'info'
    manager_name = 'manager_name'
    assistant_name = 'assistant_name'
    street_other = 'street_other'
    postal_code_other = 'postal_code_other'
    city_other = 'city_other'
    state_other = 'state_other'
    country_other = 'country_other'
    telephone_business1 = 'telephone_business1'
    telephone_business2 = 'telephone_business2'
    fax_business = 'fax_business'
    telephone_callback = 'telephone_callback'
    telephone_car = 'telephone_car'
    telephone_company = 'telephone_company'
    telephone_home1 = 'telephone_home1'
    telephone_home2 = 'telephone_home2'
    fax_home = 'fax_home'
    cellular_telephone1 = 'cellular_telephone1'
    cellular_telephone2 = 'cellular_telephone2'
    telephone_other = 'telephone_other'
    fax_other = 'fax_other'
    email1 = 'email1'
    email2 = 'email2'
    email3 = 'email3'
    url = 'url'
    telephone_isdn = 'telephone_isdn'
    telephone_pager = 'telephone_pager'
    telephone_primary = 'telephone_primary'
    telephone_radio = 'telephone_radio'
    telephone_telex = 'telephone_telex'
    telephone_ttytdd = 'telephone_ttytdd'
    instant_messenger1 = 'instant_messenger1'
    instant_messenger2 = 'instant_messenger2'
    telephone_ip = 'telephone_ip'
    telephone_assistant = 'telephone_assistant'
    company = 'company'
    image1 = 'image1'
    image1_content_type = 'image1_content_type'
    image1_url = 'image1_url'
    number_of_images = 'number_of_images'
    image_last_modified = 'image_last_modified'
    distribution_list = 'distribution_list'
    number_of_distribution_list = 'number_of_distribution_list'
    mark_as_distributionlist = 'mark_as_distributionlist'
    file_as = 'file_as'
    default_address = 'default_address'
    use_count = 'useCount'
    yomi_first_name = 'yomiFirstName'
    yomi_last_name = 'yomiLastName'
    yomi_company = 'yomiCompany'
    address_home = 'addressHome'
    address_business = 'addressBusiness'
    address_other = 'addressOther'
    userfield01 = 'userfield01'
    userfield02 = 'userfield02'
    userfield03 = 'userfield03'
    userfield04 = 'userfield04'
    userfield05 = 'userfield05'
    userfield06 = 'userfield06'
    userfield07 = 'userfield07'
    userfield08 = 'userfield08'
    userfield09 = 'userfield09'
    userfield10 = 'userfield10'
    userfield11 = 'userfield11'
    userfield12 = 'userfield12'
    userfield13 = 'userfield13'
    userfield14 = 'userfield14'
    userfield15 = 'userfield15'
    userfield16 = 'userfield16'
    userfield17 = 'userfield17'
    userfield18 = 'userfield18'
    userfield19 = 'userfield19'
    userfield20 = 'userfield20'
    id = 'id'
    created_by = 'created_by'
    modified_by = 'modified_by'
    creation_date = 'creation_date'
    last_modified = 'last_modified'
    folder_id = 'folder_id'
    categories = 'categories'
    private_flag = 'private_flag'
    color_label = 'color_label'
    number_of_attachments = 'number_of_attachments'
    last_modified_of_newest_attachment_utc = 'lastModifiedOfNewestAttachmentUTC'


class Contact(AppsuiteIdModel):
    attribute_map_class = ContactAttributeMap
    attribute_types = {
        'uid': str,
        'display_name': str,
        'first_name': str,
        'last_name': str,
        'second_name': str,
        'suffix': str,
        'title': str,
        'street_home': str,
        'postal_code_home': str,
        'city_home': str,
        'state_home': str,
        'country_home': str,
        'birthday': int,
        'marital_status': str,
        'number_of_children': str,
        'profession': str,
        'nickname': str,
        'spouse_name': str,
        'anniversary': int,
        'note': str,
        'department': str,
        'position': str,
        'employee_type': str,
        'room_number': str,
        'street_business': str,
        'postal_code_business': str,
        'city_business': str,
        'state_business': str,
        'country_business': str,
        'user_id': int,
        'number_of_employees': str,
        'sales_volume': str,
        'tax_id': str,
        'commercial_register': str,
        'branches': str,
        'business_category': str,
        'info': str,
        'manager_name': str,
        'assistant_name': str,
        'street_other': str,
        'postal_code_other': str,
        'city_other': str,
        'state_other': str,
        'country_other': str,
        'telephone_business1': str,
        'telephone_business2': str,
        'fax_business': str,
        'telephone_callback': str,
        'telephone_car': str,
        'telephone_company': str,
        'telephone_home1': str,
        'telephone_home2': str,
        'fax_home': str,
        'cellular_telephone1': str,
        'cellular_telephone2': str,
        'telephone_other': str,
        'fax_other': str,
        'email1': str,
        'email2': str,
        'email3': str,
        'url': str,
        'telephone_isdn': str,
        'telephone_pager': str,
        'telephone_primary': str,
        'telephone_radio': str,
        'telephone_telex': str,
        'telephone_ttytdd': str,
        'instant_messenger1': str,
        'instant_messenger2': str,
        'telephone_ip': str,
        'telephone_assistant': str,
        'company': str,
        'image1': str,
        'image1_content_type': str,
        'image1_url': str,
        'number_of_images': int,
        'image_last_modified': int,
        'distribution_list': List[DistributionListMember],
        'number_of_distribution_list': int,
        'mark_as_distributionlist': bool,
        'file_as': str,
        'default_address': int,
        'use_count': int,
        'yomi_first_name': str,
        'yomi_last_name': str,
        'yomi_company': str,
        'address_home': str,
        'address_business': str,
        'address_other': str,
        'userfield01': str,
        'userfield02': str,
        'userfield03': str,
        'userfield04': str,
        'userfield05': str,
        'userfield06': str,
        'userfield07': str,
        'userfield08': str,
        'userfield09': str,
        'userfield10': str,
        'userfield11': str,
        'userfield12': str,
        'userfield13': str,
        'userfield14': str,
        'userfield15': str,
        'userfield16': str,
        'userfield17': str,
        'userfield18': str,
        'userfield19': str,
        'userfield20': str,
        'id': str,
        'created_by': str,
        'modified_by': str,
        'creation_date': int,
        'last_modified': int,
        'folder_id': str,
        'categories': str,
        'private_flag': bool,
        'color_label': int,
        'number_of_attachments': int,
        'last_modified_of_newest_attachment_utc': int
    }

    def __init__(self, uid=None, display_name=None, first_name=None, last_name=None, second_name=None, suffix=None,
                 title=None, street_home=None, postal_code_home=None, city_home=None, state_home=None,
                 country_home=None, birthday=None, marital_status=None, number_of_children=None, profession=None,
                 nickname=None, spouse_name=None, anniversary=None, note=None, department=None, position=None,
                 employee_type=None, room_number=None, street_business=None, postal_code_business=None,
                 city_business=None, state_business=None, country_business=None, user_id=None, number_of_employees=None,
                 sales_volume=None, tax_id=None, commercial_register=None, branches=None, business_category=None,
                 info=None, manager_name=None, assistant_name=None, street_other=None, postal_code_other=None,
                 city_other=None, state_other=None, country_other=None, telephone_business1=None,
                 telephone_business2=None, fax_business=None, telephone_callback=None, telephone_car=None,
                 telephone_company=None, telephone_home1=None, telephone_home2=None, fax_home=None,
                 cellular_telephone1=None, cellular_telephone2=None, telephone_other=None, fax_other=None, email1=None,
                 email2=None, email3=None, url=None, telephone_isdn=None, telephone_pager=None, telephone_primary=None,
                 telephone_radio=None, telephone_telex=None, telephone_ttytdd=None, instant_messenger1=None,
                 instant_messenger2=None, telephone_ip=None, telephone_assistant=None, company=None, image1=None,
                 image1_content_type=None, image1_url=None, number_of_images=None, image_last_modified=None,
                 distribution_list=None, number_of_distribution_list=None, mark_as_distributionlist=None, file_as=None,
                 default_address=None, use_count=None, yomi_first_name=None, yomi_last_name=None, yomi_company=None,
                 address_home=None, address_business=None, address_other=None, userfield01=None, userfield02=None,
                 userfield03=None, userfield04=None, userfield05=None, userfield06=None, userfield07=None,
                 userfield08=None, userfield09=None, userfield10=None, userfield11=None, userfield12=None,
                 userfield13=None, userfield14=None, userfield15=None, userfield16=None, userfield17=None,
                 userfield18=None, userfield19=None, userfield20=None, id=None, created_by=None, modified_by=None,
                 creation_date=None, last_modified=None, folder_id=None, categories=None, private_flag=None,
                 color_label=None, number_of_attachments=None, last_modified_of_newest_attachment_utc=None):
        self._uid = None
        self._display_name = None
        self._first_name = None
        self._last_name = None
        self._second_name = None
        self._suffix = None
        self._title = None
        self._street_home = None
        self._postal_code_home = None
        self._city_home = None
        self._state_home = None
        self._country_home = None
        self._birthday = None
        self._marital_status = None
        self._number_of_children = None
        self._profession = None
        self._nickname = None
        self._spouse_name = None
        self._anniversary = None
        self._note = None
        self._department = None
        self._position = None
        self._employee_type = None
        self._room_number = None
        self._street_business = None
        self._postal_code_business = None
        self._city_business = None
        self._state_business = None
        self._country_business = None
        self._user_id = None
        self._number_of_employees = None
        self._sales_volume = None
        self._tax_id = None
        self._commercial_register = None
        self._branches = None
        self._business_category = None
        self._info = None
        self._manager_name = None
        self._assistant_name = None
        self._street_other = None
        self._postal_code_other = None
        self._city_other = None
        self._state_other = None
        self._country_other = None
        self._telephone_business1 = None
        self._telephone_business2 = None
        self._fax_business = None
        self._telephone_callback = None
        self._telephone_car = None
        self._telephone_company = None
        self._telephone_home1 = None
        self._telephone_home2 = None
        self._fax_home = None
        self._cellular_telephone1 = None
        self._cellular_telephone2 = None
        self._telephone_other = None
        self._fax_other = None
        self._email1 = None
        self._email2 = None
        self._email3 = None
        self._url = None
        self._telephone_isdn = None
        self._telephone_pager = None
        self._telephone_primary = None
        self._telephone_radio = None
        self._telephone_telex = None
        self._telephone_ttytdd = None
        self._instant_messenger1 = None
        self._instant_messenger2 = None
        self._telephone_ip = None
        self._telephone_assistant = None
        self._company = None
        self._image1 = None
        self._image1_content_type = None
        self._image1_url = None
        self._number_of_images = None
        self._image_last_modified = None
        self._distribution_list = None
        self._number_of_distribution_list = None
        self._mark_as_distributionlist = None
        self._file_as = None
        self._default_address = None
        self._use_count = None
        self._yomi_first_name = None
        self._yomi_last_name = None
        self._yomi_company = None
        self._address_home = None
        self._address_business = None
        self._address_other = None
        self._userfield01 = None
        self._userfield02 = None
        self._userfield03 = None
        self._userfield04 = None
        self._userfield05 = None
        self._userfield06 = None
        self._userfield07 = None
        self._userfield08 = None
        self._userfield09 = None
        self._userfield10 = None
        self._userfield11 = None
        self._userfield12 = None
        self._userfield13 = None
        self._userfield14 = None
        self._userfield15 = None
        self._userfield16 = None
        self._userfield17 = None
        self._userfield18 = None
        self._userfield19 = None
        self._userfield20 = None
        self._id = None
        self._created_by = None
        self._modified_by = None
        self._creation_date = None
        self._last_modified = None
        self._folder_id = None
        self._categories = None
        self._private_flag = None
        self._color_label = None
        self._number_of_attachments = None
        self._last_modified_of_newest_attachment_utc = None

        if uid is not None:
            self._uid = uid
        if display_name is not None:
            self._display_name = display_name
        if first_name is not None:
            self._first_name = first_name
        if last_name is not None:
            self._last_name = last_name
        if second_name is not None:
            self._second_name = second_name
        if suffix is not None:
            self._suffix = suffix
        if title is not None:
            self._title = title
        if street_home is not None:
            self._street_home = street_home
        if postal_code_home is not None:
            self._postal_code_home = postal_code_home
        if city_home is not None:
            self._city_home = city_home
        if state_home is not None:
            self._state_home = state_home
        if country_home is not None:
            self._country_home = country_home
        if birthday is not None:
            self._birthday = birthday
        if marital_status is not None:
            self._marital_status = marital_status
        if number_of_children is not None:
            self._number_of_children = number_of_children
        if profession is not None:
            self._profession = profession
        if nickname is not None:
            self._nickname = nickname
        if spouse_name is not None:
            self._spouse_name = spouse_name
        if anniversary is not None:
            self._anniversary = anniversary
        if note is not None:
            self._note = note
        if department is not None:
            self._department = department
        if position is not None:
            self._position = position
        if employee_type is not None:
            self._employee_type = employee_type
        if room_number is not None:
            self._room_number = room_number
        if street_business is not None:
            self._street_business = street_business
        if postal_code_business is not None:
            self._postal_code_business = postal_code_business
        if city_business is not None:
            self._city_business = city_business
        if state_business is not None:
            self._state_business = state_business
        if country_business is not None:
            self._country_business = country_business
        if user_id is not None:
            self._user_id = user_id
        if number_of_employees is not None:
            self._number_of_employees = number_of_employees
        if sales_volume is not None:
            self._sales_volume = sales_volume
        if tax_id is not None:
            self._tax_id = tax_id
        if commercial_register is not None:
            self._commercial_register = commercial_register
        if branches is not None:
            self._branches = branches
        if business_category is not None:
            self._business_category = business_category
        if info is not None:
            self._info = info
        if manager_name is not None:
            self._manager_name = manager_name
        if assistant_name is not None:
            self._assistant_name = assistant_name
        if street_other is not None:
            self._street_other = street_other
        if postal_code_other is not None:
            self._postal_code_other = postal_code_other
        if city_other is not None:
            self._city_other = city_other
        if state_other is not None:
            self._state_other = state_other
        if country_other is not None:
            self._country_other = country_other
        if telephone_business1 is not None:
            self._telephone_business1 = telephone_business1
        if telephone_business2 is not None:
            self._telephone_business2 = telephone_business2
        if fax_business is not None:
            self._fax_business = fax_business
        if telephone_callback is not None:
            self._telephone_callback = telephone_callback
        if telephone_car is not None:
            self._telephone_car = telephone_car
        if telephone_company is not None:
            self._telephone_company = telephone_company
        if telephone_home1 is not None:
            self._telephone_home1 = telephone_home1
        if telephone_home2 is not None:
            self._telephone_home2 = telephone_home2
        if fax_home is not None:
            self._fax_home = fax_home
        if cellular_telephone1 is not None:
            self._cellular_telephone1 = cellular_telephone1
        if cellular_telephone2 is not None:
            self._cellular_telephone2 = cellular_telephone2
        if telephone_other is not None:
            self._telephone_other = telephone_other
        if fax_other is not None:
            self._fax_other = fax_other
        if email1 is not None:
            self._email1 = email1
        if email2 is not None:
            self._email2 = email2
        if email3 is not None:
            self._email3 = email3
        if url is not None:
            self._url = url
        if telephone_isdn is not None:
            self._telephone_isdn = telephone_isdn
        if telephone_pager is not None:
            self._telephone_pager = telephone_pager
        if telephone_primary is not None:
            self._telephone_primary = telephone_primary
        if telephone_radio is not None:
            self._telephone_radio = telephone_radio
        if telephone_telex is not None:
            self._telephone_telex = telephone_telex
        if telephone_ttytdd is not None:
            self._telephone_ttytdd = telephone_ttytdd
        if instant_messenger1 is not None:
            self._instant_messenger1 = instant_messenger1
        if instant_messenger2 is not None:
            self._instant_messenger2 = instant_messenger2
        if telephone_ip is not None:
            self._telephone_ip = telephone_ip
        if telephone_assistant is not None:
            self._telephone_assistant = telephone_assistant
        if company is not None:
            self._company = company
        if image1 is not None:
            self._image1 = image1
        if image1_content_type is not None:
            self._image1_content_type = image1_content_type
        if image1_url is not None:
            self._image1_url = image1_url
        if number_of_images is not None:
            self._number_of_images = number_of_images
        if image_last_modified is not None:
            self._image_last_modified = image_last_modified
        if distribution_list is not None:
            self._distribution_list = distribution_list
        if number_of_distribution_list is not None:
            self._number_of_distribution_list = number_of_distribution_list
        if mark_as_distributionlist is not None:
            self._mark_as_distributionlist = mark_as_distributionlist
        if file_as is not None:
            self._file_as = file_as
        if default_address is not None:
            self._default_address = default_address
        if use_count is not None:
            self._use_count = use_count
        if yomi_first_name is not None:
            self._yomi_first_name = yomi_first_name
        if yomi_last_name is not None:
            self._yomi_last_name = yomi_last_name
        if yomi_company is not None:
            self._yomi_company = yomi_company
        if address_home is not None:
            self._address_home = address_home
        if address_business is not None:
            self._address_business = address_business
        if address_other is not None:
            self._address_other = address_other
        if userfield01 is not None:
            self._userfield01 = userfield01
        if userfield02 is not None:
            self._userfield02 = userfield02
        if userfield03 is not None:
            self._userfield03 = userfield03
        if userfield04 is not None:
            self._userfield04 = userfield04
        if userfield05 is not None:
            self._userfield05 = userfield05
        if userfield06 is not None:
            self._userfield06 = userfield06
        if userfield07 is not None:
            self._userfield07 = userfield07
        if userfield08 is not None:
            self._userfield08 = userfield08
        if userfield09 is not None:
            self._userfield09 = userfield09
        if userfield10 is not None:
            self._userfield10 = userfield10
        if userfield11 is not None:
            self._userfield11 = userfield11
        if userfield12 is not None:
            self._userfield12 = userfield12
        if userfield13 is not None:
            self._userfield13 = userfield13
        if userfield14 is not None:
            self._userfield14 = userfield14
        if userfield15 is not None:
            self._userfield15 = userfield15
        if userfield16 is not None:
            self._userfield16 = userfield16
        if userfield17 is not None:
            self._userfield17 = userfield17
        if userfield18 is not None:
            self._userfield18 = userfield18
        if userfield19 is not None:
            self._userfield19 = userfield19
        if userfield20 is not None:
            self._userfield20 = userfield20
        if id is not None:
            self._id = id
        if created_by is not None:
            self._created_by = created_by
        if modified_by is not None:
            self._modified_by = modified_by
        if creation_date is not None:
            self._creation_date = creation_date
        if last_modified is not None:
            self._last_modified = last_modified
        if folder_id is not None:
            self._folder_id = folder_id
        if categories is not None:
            self._categories = categories
        if private_flag is not None:
            self._private_flag = private_flag
        if color_label is not None:
            self._color_label = color_label
        if number_of_attachments is not None:
            self._number_of_attachments = number_of_attachments
        if last_modified_of_newest_attachment_utc is not None:
            self._last_modified_of_newest_attachment_utc = last_modified_of_newest_attachment_utc

    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, uid):
        self._uid = uid

    @property
    def display_name(self):
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        self._display_name = display_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @property
    def second_name(self):
        return self._second_name

    @second_name.setter
    def second_name(self, second_name):
        self._second_name = second_name

    @property
    def suffix(self):
        return self._suffix

    @suffix.setter
    def suffix(self, suffix):
        self._suffix = suffix

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def street_home(self):
        return self._street_home

    @street_home.setter
    def street_home(self, street_home):
        self._street_home = street_home

    @property
    def postal_code_home(self):
        return self._postal_code_home

    @postal_code_home.setter
    def postal_code_home(self, postal_code_home):
        self._postal_code_home = postal_code_home

    @property
    def city_home(self):
        return self._city_home

    @city_home.setter
    def city_home(self, city_home):
        self._city_home = city_home

    @property
    def state_home(self):
        return self._state_home

    @state_home.setter
    def state_home(self, state_home):
        self._state_home = state_home

    @property
    def country_home(self):
        return self._country_home

    @country_home.setter
    def country_home(self, country_home):
        self._country_home = country_home

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, birthday):
        self._birthday = birthday

    @property
    def marital_status(self):
        return self._marital_status

    @marital_status.setter
    def marital_status(self, marital_status):
        self._marital_status = marital_status

    @property
    def number_of_children(self):
        return self._number_of_children

    @number_of_children.setter
    def number_of_children(self, number_of_children):
        self._number_of_children = number_of_children

    @property
    def profession(self):
        return self._profession

    @profession.setter
    def profession(self, profession):
        self._profession = profession

    @property
    def nickname(self):
        return self._nickname

    @nickname.setter
    def nickname(self, nickname):
        self._nickname = nickname

    @property
    def spouse_name(self):
        return self._spouse_name

    @spouse_name.setter
    def spouse_name(self, spouse_name):
        self._spouse_name = spouse_name

    @property
    def anniversary(self):
        return self._anniversary

    @anniversary.setter
    def anniversary(self, anniversary):
        self._anniversary = anniversary

    @property
    def note(self):
        return self._note

    @note.setter
    def note(self, note):
        self._note = note

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, department):
        self._department = department

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        self._position = position

    @property
    def employee_type(self):
        return self._employee_type

    @employee_type.setter
    def employee_type(self, employee_type):
        self._employee_type = employee_type

    @property
    def room_number(self):
        return self._room_number

    @room_number.setter
    def room_number(self, room_number):
        self._room_number = room_number

    @property
    def street_business(self):
        return self._street_business

    @street_business.setter
    def street_business(self, street_business):
        self._street_business = street_business

    @property
    def postal_code_business(self):
        return self._postal_code_business

    @postal_code_business.setter
    def postal_code_business(self, postal_code_business):
        self._postal_code_business = postal_code_business

    @property
    def city_business(self):
        return self._city_business

    @city_business.setter
    def city_business(self, city_business):
        self._city_business = city_business

    @property
    def state_business(self):
        return self._state_business

    @state_business.setter
    def state_business(self, state_business):
        self._state_business = state_business

    @property
    def country_business(self):
        return self._country_business

    @country_business.setter
    def country_business(self, country_business):
        self._country_business = country_business

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        self._user_id = user_id

    @property
    def number_of_employees(self):
        return self._number_of_employees

    @number_of_employees.setter
    def number_of_employees(self, number_of_employees):
        self._number_of_employees = number_of_employees

    @property
    def sales_volume(self):
        return self._sales_volume

    @sales_volume.setter
    def sales_volume(self, sales_volume):
        self._sales_volume = sales_volume

    @property
    def tax_id(self):
        return self._tax_id

    @tax_id.setter
    def tax_id(self, tax_id):
        self._tax_id = tax_id

    @property
    def commercial_register(self):
        return self._commercial_register

    @commercial_register.setter
    def commercial_register(self, commercial_register):
        self._commercial_register = commercial_register

    @property
    def branches(self):
        return self._branches

    @branches.setter
    def branches(self, branches):
        self._branches = branches

    @property
    def business_category(self):
        return self._business_category

    @business_category.setter
    def business_category(self, business_category):
        self._business_category = business_category

    @property
    def info(self):
        return self._info

    @info.setter
    def info(self, info):
        self._info = info

    @property
    def manager_name(self):
        return self._manager_name

    @manager_name.setter
    def manager_name(self, manager_name):
        self._manager_name = manager_name

    @property
    def assistant_name(self):
        return self._assistant_name

    @assistant_name.setter
    def assistant_name(self, assistant_name):
        self._assistant_name = assistant_name

    @property
    def street_other(self):
        return self._street_other

    @street_other.setter
    def street_other(self, street_other):
        self._street_other = street_other

    @property
    def postal_code_other(self):
        return self._postal_code_other

    @postal_code_other.setter
    def postal_code_other(self, postal_code_other):
        self._postal_code_other = postal_code_other

    @property
    def city_other(self):
        return self._city_other

    @city_other.setter
    def city_other(self, city_other):
        self._city_other = city_other

    @property
    def state_other(self):
        return self._state_other

    @state_other.setter
    def state_other(self, state_other):
        self._state_other = state_other

    @property
    def country_other(self):
        return self._country_other

    @country_other.setter
    def country_other(self, country_other):
        self._country_other = country_other

    @property
    def telephone_business1(self):
        return self._telephone_business1

    @telephone_business1.setter
    def telephone_business1(self, telephone_business1):
        self._telephone_business1 = telephone_business1

    @property
    def telephone_business2(self):
        return self._telephone_business2

    @telephone_business2.setter
    def telephone_business2(self, telephone_business2):
        self._telephone_business2 = telephone_business2

    @property
    def fax_business(self):
        return self._fax_business

    @fax_business.setter
    def fax_business(self, fax_business):
        self._fax_business = fax_business

    @property
    def telephone_callback(self):
        return self._telephone_callback

    @telephone_callback.setter
    def telephone_callback(self, telephone_callback):
        self._telephone_callback = telephone_callback

    @property
    def telephone_car(self):
        return self._telephone_car

    @telephone_car.setter
    def telephone_car(self, telephone_car):
        self._telephone_car = telephone_car

    @property
    def telephone_company(self):
        return self._telephone_company

    @telephone_company.setter
    def telephone_company(self, telephone_company):
        self._telephone_company = telephone_company

    @property
    def telephone_home1(self):
        return self._telephone_home1

    @telephone_home1.setter
    def telephone_home1(self, telephone_home1):
        self._telephone_home1 = telephone_home1

    @property
    def telephone_home2(self):
        return self._telephone_home2

    @telephone_home2.setter
    def telephone_home2(self, telephone_home2):
        self._telephone_home2 = telephone_home2

    @property
    def fax_home(self):
        return self._fax_home

    @fax_home.setter
    def fax_home(self, fax_home):
        self._fax_home = fax_home

    @property
    def cellular_telephone1(self):
        return self._cellular_telephone1

    @cellular_telephone1.setter
    def cellular_telephone1(self, cellular_telephone1):
        self._cellular_telephone1 = cellular_telephone1

    @property
    def cellular_telephone2(self):
        return self._cellular_telephone2

    @cellular_telephone2.setter
    def cellular_telephone2(self, cellular_telephone2):
        self._cellular_telephone2 = cellular_telephone2

    @property
    def telephone_other(self):
        return self._telephone_other

    @telephone_other.setter
    def telephone_other(self, telephone_other):
        self._telephone_other = telephone_other

    @property
    def fax_other(self):
        return self._fax_other

    @fax_other.setter
    def fax_other(self, fax_other):
        self._fax_other = fax_other

    @property
    def email1(self):
        return self._email1

    @email1.setter
    def email1(self, email1):
        self._email1 = email1

    @property
    def email2(self):
        return self._email2

    @email2.setter
    def email2(self, email2):
        self._email2 = email2

    @property
    def email3(self):
        return self._email3

    @email3.setter
    def email3(self, email3):
        self._email3 = email3

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url

    @property
    def telephone_isdn(self):
        return self._telephone_isdn

    @telephone_isdn.setter
    def telephone_isdn(self, telephone_isdn):
        self._telephone_isdn = telephone_isdn

    @property
    def telephone_pager(self):
        return self._telephone_pager

    @telephone_pager.setter
    def telephone_pager(self, telephone_pager):
        self._telephone_pager = telephone_pager

    @property
    def telephone_primary(self):
        return self._telephone_primary

    @telephone_primary.setter
    def telephone_primary(self, telephone_primary):
        self._telephone_primary = telephone_primary

    @property
    def telephone_radio(self):
        return self._telephone_radio

    @telephone_radio.setter
    def telephone_radio(self, telephone_radio):
        self._telephone_radio = telephone_radio

    @property
    def telephone_telex(self):
        return self._telephone_telex

    @telephone_telex.setter
    def telephone_telex(self, telephone_telex):
        self._telephone_telex = telephone_telex

    @property
    def telephone_ttytdd(self):
        return self._telephone_ttytdd

    @telephone_ttytdd.setter
    def telephone_ttytdd(self, telephone_ttytdd):
        self._telephone_ttytdd = telephone_ttytdd

    @property
    def instant_messenger1(self):
        return self._instant_messenger1

    @instant_messenger1.setter
    def instant_messenger1(self, instant_messenger1):
        self._instant_messenger1 = instant_messenger1

    @property
    def instant_messenger2(self):
        return self._instant_messenger2

    @instant_messenger2.setter
    def instant_messenger2(self, instant_messenger2):
        self._instant_messenger2 = instant_messenger2

    @property
    def telephone_ip(self):
        return self._telephone_ip

    @telephone_ip.setter
    def telephone_ip(self, telephone_ip):
        self._telephone_ip = telephone_ip

    @property
    def telephone_assistant(self):
        return self._telephone_assistant

    @telephone_assistant.setter
    def telephone_assistant(self, telephone_assistant):
        self._telephone_assistant = telephone_assistant

    @property
    def company(self):
        return self._company

    @company.setter
    def company(self, company):
        self._company = company

    @property
    def image1(self):
        return self._image1

    @image1.setter
    def image1(self, image1):
        self._image1 = image1

    @property
    def image1_content_type(self):
        return self._image1_content_type

    @image1_content_type.setter
    def image1_content_type(self, image1_content_type):
        self._image1_content_type = image1_content_type

    @property
    def image1_url(self):
        return self._image1_url

    @image1_url.setter
    def image1_url(self, image1_url):
        self._image1_url = image1_url

    @property
    def number_of_images(self):
        return self._number_of_images

    @number_of_images.setter
    def number_of_images(self, number_of_images):
        self._number_of_images = number_of_images

    @property
    def image_last_modified(self):
        return self._image_last_modified

    @image_last_modified.setter
    def image_last_modified(self, image_last_modified):
        self._image_last_modified = image_last_modified

    @property
    def distribution_list(self):
        return self._distribution_list

    @distribution_list.setter
    def distribution_list(self, distribution_list):
        self._distribution_list = distribution_list

    @property
    def number_of_distribution_list(self):
        return self._number_of_distribution_list

    @number_of_distribution_list.setter
    def number_of_distribution_list(self, number_of_distribution_list):
        self._number_of_distribution_list = number_of_distribution_list

    @property
    def mark_as_distributionlist(self):
        return self._mark_as_distributionlist

    @mark_as_distributionlist.setter
    def mark_as_distributionlist(self, mark_as_distributionlist):
        self._mark_as_distributionlist = mark_as_distributionlist

    @property
    def file_as(self):
        return self._file_as

    @file_as.setter
    def file_as(self, file_as):
        self._file_as = file_as

    @property
    def default_address(self):
        return self._default_address

    @default_address.setter
    def default_address(self, default_address):
        self._default_address = default_address

    @property
    def use_count(self):
        return self._use_count

    @use_count.setter
    def use_count(self, use_count):
        self._use_count = use_count

    @property
    def yomi_first_name(self):
        return self._yomi_first_name

    @yomi_first_name.setter
    def yomi_first_name(self, yomi_first_name):
        self._yomi_first_name = yomi_first_name

    @property
    def yomi_last_name(self):
        return self._yomi_last_name

    @yomi_last_name.setter
    def yomi_last_name(self, yomi_last_name):
        self._yomi_last_name = yomi_last_name

    @property
    def yomi_company(self):
        return self._yomi_company

    @yomi_company.setter
    def yomi_company(self, yomi_company):
        self._yomi_company = yomi_company

    @property
    def address_home(self):
        return self._address_home

    @address_home.setter
    def address_home(self, address_home):
        self._address_home = address_home

    @property
    def address_business(self):
        return self._address_business

    @address_business.setter
    def address_business(self, address_business):
        self._address_business = address_business

    @property
    def address_other(self):
        return self._address_other

    @address_other.setter
    def address_other(self, address_other):
        self._address_other = address_other

    @property
    def userfield01(self):
        return self._userfield01

    @userfield01.setter
    def userfield01(self, userfield01):
        self._userfield01 = userfield01

    @property
    def userfield02(self):
        return self._userfield02

    @userfield02.setter
    def userfield02(self, userfield02):
        self._userfield02 = userfield02

    @property
    def userfield03(self):
        return self._userfield03

    @userfield03.setter
    def userfield03(self, userfield03):
        self._userfield03 = userfield03

    @property
    def userfield04(self):
        return self._userfield04

    @userfield04.setter
    def userfield04(self, userfield04):
        self._userfield04 = userfield04

    @property
    def userfield05(self):
        return self._userfield05

    @userfield05.setter
    def userfield05(self, userfield05):
        self._userfield05 = userfield05

    @property
    def userfield06(self):
        return self._userfield06

    @userfield06.setter
    def userfield06(self, userfield06):
        self._userfield06 = userfield06

    @property
    def userfield07(self):
        return self._userfield07

    @userfield07.setter
    def userfield07(self, userfield07):
        self._userfield07 = userfield07

    @property
    def userfield08(self):
        return self._userfield08

    @userfield08.setter
    def userfield08(self, userfield08):
        self._userfield08 = userfield08

    @property
    def userfield09(self):
        return self._userfield09

    @userfield09.setter
    def userfield09(self, userfield09):
        self._userfield09 = userfield09

    @property
    def userfield10(self):
        return self._userfield10

    @userfield10.setter
    def userfield10(self, userfield10):
        self._userfield10 = userfield10

    @property
    def userfield11(self):
        return self._userfield11

    @userfield11.setter
    def userfield11(self, userfield11):
        self._userfield11 = userfield11

    @property
    def userfield12(self):
        return self._userfield12

    @userfield12.setter
    def userfield12(self, userfield12):
        self._userfield12 = userfield12

    @property
    def userfield13(self):
        return self._userfield13

    @userfield13.setter
    def userfield13(self, userfield13):
        self._userfield13 = userfield13

    @property
    def userfield14(self):
        return self._userfield14

    @userfield14.setter
    def userfield14(self, userfield14):
        self._userfield14 = userfield14

    @property
    def userfield15(self):
        return self._userfield15

    @userfield15.setter
    def userfield15(self, userfield15):
        self._userfield15 = userfield15

    @property
    def userfield16(self):
        return self._userfield16

    @userfield16.setter
    def userfield16(self, userfield16):
        self._userfield16 = userfield16

    @property
    def userfield17(self):
        return self._userfield17

    @userfield17.setter
    def userfield17(self, userfield17):
        self._userfield17 = userfield17

    @property
    def userfield18(self):
        return self._userfield18

    @userfield18.setter
    def userfield18(self, userfield18):
        self._userfield18 = userfield18

    @property
    def userfield19(self):
        return self._userfield19

    @userfield19.setter
    def userfield19(self, userfield19):
        self._userfield19 = userfield19

    @property
    def userfield20(self):
        return self._userfield20

    @userfield20.setter
    def userfield20(self, userfield20):
        self._userfield20 = userfield20

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def created_by(self):
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        self._created_by = created_by

    @property
    def modified_by(self):
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        self._modified_by = modified_by

    @property
    def creation_date(self):
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        self._creation_date = creation_date

    @property
    def last_modified(self):
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        self._last_modified = last_modified

    @property
    def folder_id(self):
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        self._folder_id = folder_id

    @property
    def categories(self):
        return self._categories

    @categories.setter
    def categories(self, categories):
        self._categories = categories

    @property
    def private_flag(self):
        return self._private_flag

    @private_flag.setter
    def private_flag(self, private_flag):
        self._private_flag = private_flag

    @property
    def color_label(self):
        return self._color_label

    @color_label.setter
    def color_label(self, color_label):
        if color_label is not None and color_label > 10:
            raise ValueError("Invalid value for `color_label`, must be a value less than or equal to `10`")
        if color_label is not None and color_label < 0:
            raise ValueError("Invalid value for `color_label`, must be a value greater than or equal to `0`")

        self._color_label = color_label

    @property
    def number_of_attachments(self):
        return self._number_of_attachments

    @number_of_attachments.setter
    def number_of_attachments(self, number_of_attachments):
        self._number_of_attachments = number_of_attachments

    @property
    def last_modified_of_newest_attachment_utc(self):
        return self._last_modified_of_newest_attachment_utc

    @last_modified_of_newest_attachment_utc.setter
    def last_modified_of_newest_attachment_utc(self, last_modified_of_newest_attachment_utc):
        self._last_modified_of_newest_attachment_utc = last_modified_of_newest_attachment_utc
