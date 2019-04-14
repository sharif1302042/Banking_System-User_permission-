from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.mixins import PermissionRequiredMixin

from USERs.models import Account, Topup, TranferBalance  # ,Payment
from .serializers import AccountSerializer, TransferBalanceSerializer,TopUpSerializer,Userserializer

class Uerlist(APIView):
    def get(self,request, *args, **kwargs):
        if request.user.has_perm('USERs.Can view user'):
            users = User.objects.all()
            serializer = Userserializer(users , many=True)
            return Response(serializer.data)
        return Response("No Permission",status= status.HTTP_400_BAD_REQUEST)


class Accountlist(APIView):
    def get(self, request, *args, **kwargs):
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        account = Account.objects.create(
            account_number=request.data['account_number'],
            name=request.data['name'],
            phone_number=request.data['phone_number'],
            balance=request.data['balance'],
        )
        if account:
            return Response("Account Created Successfully", status=status.HTTP_201_CREATED)
        return Response("Failed", status=status.HTTP_400_BAD_REQUEST)


class TopUP(APIView):
    def post(self,request,*args,**kwargs):
        serializer = TopUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            amount = serializer.data['amount']
            try:
                account = Account.objects.get(account_number=request.data['topup_account_number'])
                if float(account.balance)<=float(amount):
                    return Response("Insufficient Balance!!!", status=status.HTTP_400_BAD_REQUEST)
                account.balance =float(account.balance)-float(amount)
                account.save()
                return Response("Top up Successfull!!!", status=status.HTTP_400_BAD_REQUEST)
            except:
                return Response("Account Doesnot exists!!!", status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BalanceTransfer(APIView):
    def post(self,request,*args,**kwargs):
        try:
            debit_account = Account.objects.get(account_number=request.data['debit_account'])
            credit_account = Account.objects.get(account_number=request.data['credit_account'])
            amount = request.data['amount']
            t_type = request.data['transection_type']

            if debit_account.balance < float(amount):
                return Response("Insufficient Balance!!!", status=status.HTTP_400_BAD_REQUEST)

            debit_account.balance = float(debit_account.balance) - float(amount)
            credit_account.balance = float(credit_account.balance) + float(amount)

            tb = TranferBalance.objects.create(
                debit_account = debit_account,
                credit_account = credit_account,
                amount = amount,
                transection_type = t_type,
            )
            if tb:
                debit_account.save()
                credit_account.save()
                return Response("Balance Transfered Successfully", status=status.HTTP_201_CREATED)

        except:
            return Response("Invalid account!!!", status=status.HTTP_400_BAD_REQUEST)










"""
class BalanceTransfer(APIView):
    def post(self, request, *args, **kwargs):
        serializer = TransferBalanceSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            debit_acc = serializer.data['debit_account']
            credit_acc = serializer.data['credit_account']
            amount = serializer.data['amount']
            t_type = serializer.data['transection_type']
            try:
                dr = Account.objects.get(account_number=debit_acc)
                cr = Account.objects.get(account_number=credit_acc)
                if dr.balance < float(amount):
                    return Response("Insufficient Balance!!!", status=status.HTTP_400_BAD_REQUEST)

                dr.balance =float(dr.balance)-float(amount)
                cr.balance = float(cr.balance)+float(amount)

                dr.save()
                cr.save()
                return Response("Transection Succesful!!!", status=status.HTTP_201_CREATED)

            except:
                return Response("Invalid account!!!", status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""




