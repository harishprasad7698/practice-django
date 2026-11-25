from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class BmiCalculatorView(View):
    def post(self,request):
        data=json.loads(request.body)
        height=(data.get("height"))/100
        weight=data.get("weight")
        return JsonResponse({"height":data.get("height"),
                             "weight":weight,
                             "bmi":round((weight/height**2),2)})
        
@method_decorator(csrf_exempt,name='dispatch')
class AgeCalaculatorView(View):
    def post(self,request):
        data =json.loads(request.body)
        birth_year=data.get("birth_year")
        current_year=data.get("current_year")
        return JsonResponse({"age":current_year-birth_year})
    
    
@method_decorator(csrf_exempt,name='dispatch')
class PercentageCalcView(View):
    def post(self,request):
        data=json.loads(request.body)
        return JsonResponse({"percentage":(data.get("obtained_marks")/data.get("total_marks"))*100})
    
@method_decorator(csrf_exempt,name='dispatch')
class SimpleInterestView(View):
    def post(self,request):
        data=json.loads(request.body)
        si=(data.get("principal")*data.get("rate")*data.get("time"))/100
        return JsonResponse(
            {
                "principal":data.get("principal"),
                "rate":data.get("rate"),
                "time":data.get("time"),
                "si":si
            }
        )


@method_decorator(csrf_exempt,name='dispatch')
class ElectricityView(View):
    def post(self,request):
        data=json.loads(request.body)
        bill=(data.get("price")*data.get("units"))
        return JsonResponse(
            {
                "price":data.get("price"),
                "units":data.get("units"),
                "bill":bill
            }
        )
@method_decorator(csrf_exempt,name='dispatch')
class DiscountView(View):
    def post(self,request):
        data=json.loads(request.body)
        discount=(data.get("price")*data.get("discount_percent"))/100
        final_price=data.get("price")-discount
        
        return JsonResponse(
            {
                "price":data.get("price"),
                "discount_percentage":data.get("discount_percent"),
                "discount_amount":discount,
                "final_price":final_price
            }
        )
        
        
@method_decorator(csrf_exempt,name='dispatch')
class ProfitView(View):
    def post(self,request):
        data=json.loads(request.body)
        profit=data.get("selling_price")-data.get("cost_price")
        
        return JsonResponse(
            {
                "cost_price":data.get("cost_price"),
                "selling_price":data.get("selling_price"),
                "profit":profit
            }
        )
        
@method_decorator(csrf_exempt,name='dispatch')
class SalaryView(View):
    def post(self,request):
        data=json.loads(request.body)
        net_salary=data.get("basic_salary")+data.get("bonus")-data.get("deduction")
        
        return JsonResponse(
            {
                "basic_salary":data.get("basic_salary"),
                "bonus":data.get("bonus"),
                "deduction":data.get("deduction"),
                "net_salary":net_salary,
            }
        )
    
@method_decorator(csrf_exempt,name='dispatch')
class TimeView(View):
    def post(self,request):
        data=json.loads(request.body)
        
        return JsonResponse(
            {
                "hours":data.get("hours"),
                "minutes":data.get("hours")*60,
                "seconds":data.get("hours")*3600
                
            }
        )
       
@method_decorator(csrf_exempt,name='dispatch') 
class FuelView(View):
    def post(self,request):
        data=json.loads(request.body)
        fuel_required=(data.get("distance")/data.get("mileage"))
        total_cost=data.get("fuel_price")*fuel_required
        
        return JsonResponse(
            {
                "distance":data.get("distance"),
                "mileage":data.get("mileage"),
                "fuel_price":data.get("fuel_price"),
                "fuel_required":fuel_required,
                "total_cost":total_cost
            }
        )
        
@method_decorator(csrf_exempt,name='dispatch') 
class ProductProfitView(View):
    def post(self,request):
        data=json.loads(request.body)
        total_cost=(data.get("cost_price")*data.get("quantity"))
        total_sales=data.get("selling_price")*data.get("quantity")
        Profit=total_sales-total_cost
        return JsonResponse(
            {
                "cost_price":data.get("cost_price"),
                "selling_price":data.get("selling_price"),
                "quantity":data.get("quantity"),
                "total_cost":total_cost,
                "total_sales":total_sales,
                "profit":Profit
            }
        )
        
@method_decorator(csrf_exempt,name='dispatch') 
class AgeDetailsView(View):
    def post(self,request):
        data=json.loads(request.body)
        months=(data.get("age")*12)
        weeks=data.get("age")*52
        days=data.get("age")*365
        return JsonResponse(
            {
                "age":data.get("age"),
                "months":months,
                "weeks":weeks,
                "days":days
                
            }
        )