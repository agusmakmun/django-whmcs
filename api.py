#!/usr/bin/python

from clients import Client
from connection import APIConn

import md5


class WHMCS:
    
    data = {}

    def send_call(self):
        # this function should handle all errors
        conn = APIConn()
        resp = conn.request(self.data)
        return resp

    # CLIENT API CALLS
    def client_get_set(self, limitstart=0, limitnum=25, search=None):

        self.data['action'] = 'getclients'
        self.data['limitnum'] = limitnum
        self.data['limitstart'] = limitstart
        if search is not None:
            self.data['search'] = search

        data = self.send_call()

        if data['result'] == 'success' and int(data['numreturned']) == 0:
            return []

        clients = data['clients']['client']

        client_list = []
        for client in clients:
            client_list.append(Client(data=client))
        return client_list

    def client_get_details(self, client_id, email=None):
        
        self.data['action'] = 'getclientsdetails'
        self.data['clientid'] = client_id
        if email is not None:
            self.data['email'] = email

        data = self.send_call()
        return Client(data=data)

    def client_get_password(self, client_id):
        
        self.data['action']   = 'getclientpassword'
        self.data['userid'] = client_id
        data = self.send_call()
        
        if data['result'] != 'success':
            return None

        return data['password'].split(':')

    def client_check_password(self, client_id, password):
        
        (db_password, salt) = self.client_get_password(client_id)
        m = md5.new()
        m.update(salt)
        m.update(password)
        
        md5_password = m.hexdigest()

        if md5_password == db_password:
            return True
        return False

    # ORDER API CALLS
    def order_get_set(self,
                      limitstart=0,
                      limitnum=25,
                      id=None,
                      userid=None,
                      status=None):
        
        self.data['action'] = "getorders"
        self.data['limitnum'] = limitnum
        self.data['limitstart'] = limitstart
        if id is not None:
            self.data['id'] = id
        if userid is not None:
            self.data['userid'] = userid
        if status is not None:
            self.data['status'] = status

        data = self.send_call()
