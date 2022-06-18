import http

from django.shortcuts import render
from django.http import JsonResponse
import logging
import hexbytes
import SimpleBankApp.resources.core as core
import SimpleBankApp.resources.accounts as accounts
import SimpleBankApp.resources.appConfig as appConfig
import SimpleBankApp.resources.utilities as utilities
from decimal import *
from django.http import JsonResponse
from django.http import HttpResponseServerError
from django.http import HttpResponse
# Create your views here.
logger = logging.getLogger(__name__)


def home(req):
    resp = ""
    if req.method == 'GET':
        try:
            user_accts = accounts.get_all_accounts()
            params = {"accounts": user_accts, "contract_address": appConfig.contract_address,
                      "contract_balance": core.get_ether_balance(appConfig.contract_address)}
            resp = render(request=req, template_name='index.html', context=params)
        except Exception as ex:
            resp = JsonResponse({'error': str(ex)}, status=500)
    return resp


def deposit(req):
    resp = ""
    if req.method == 'POST':
        try:
            deposit_from_addr_index = int(req.POST.get('deposit_from_addr', ''))
            deposit_qty = Decimal(req.POST.get('deposit_qty', ''))
            tx_receipt, events = core.deposit(deposit_from_addr_index, deposit_qty)
            params = {"txReceipt": dict(tx_receipt), "events": list(events)}
            params = utilities.dict_to_json_serializable(params)
            resp = JsonResponse(params)
        except Exception as ex:
            resp = JsonResponse({'error': str(ex)}, status=500)
    return resp


def grant_allowance(req):
    resp = ""
    if req.method == 'POST':
        try:
            grant_from_addr_index = int(req.POST.get('grant_from_addr', ''))
            grant_to_addr_index = int(req.POST.get('grant_to_addr', ''))
            grant_qty = Decimal(req.POST.get('grant_qty', ''))
            tx_receipt, events = core.grant_allowance(grant_from_addr_index, grant_to_addr_index, grant_qty)
            params = {"txReceipt": dict(tx_receipt), "events": list(events)}
            params = utilities.dict_to_json_serializable(params)
            resp = JsonResponse(params)
        except Exception as ex:
            resp = JsonResponse({'error': str(ex)}, status=500)
    return resp


def withdraw(req):
    resp = ""
    if req.method == 'POST':
        try:
            withdraw_addr_index = int(req.POST.get('withdraw_addr', ''))
            withdraw_qty = Decimal(req.POST.get('withdraw_qty', ''))
            tx_receipt, events = core.withdraw(withdraw_addr_index, withdraw_qty)
            params = {"txReceipt": dict(tx_receipt), "events": list(events)}
            params = utilities.dict_to_json_serializable(params)
            resp = JsonResponse(params)
        except Exception as ex:
            resp = JsonResponse({'error': str(ex)}, status=500)
    return resp


def get_allowance(req):
    resp = ""
    if req.method == 'POST':
        try:
            user_addr_index = int(req.POST.get('user_addr', ''))
            allowance = core.get_allowance(user_addr_index)
            params = {"allowance": allowance}
            resp = JsonResponse(params)
        except Exception as ex:
            resp = JsonResponse({'error': str(ex)}, status=500)
    return resp


def get_balance(req):
    resp = ""
    if req.method == 'POST':
        try:
            user_acct_index = int(req.POST.get('from_addr', ''))
            user_acct = accounts.import_account_from_config(user_acct_index)
            balance = core.get_ether_balance(user_acct['address'])
            params = {"balance": balance}
            params = utilities.dict_to_json_serializable(params)
            resp = JsonResponse(params)
        except Exception as ex:
            resp = JsonResponse({'error': str(ex)}, status=500)
    return resp


def get_contract_balance(req):
    resp = ""
    if req.method == 'GET':
        try:
            balance = core.get_ether_balance(appConfig.contract_address)
            params = {"balance": balance}
            params = utilities.dict_to_json_serializable(params)
            resp = JsonResponse(params)
        except Exception as ex:
            resp = JsonResponse({'error': str(ex)}, status=500)
    return resp
