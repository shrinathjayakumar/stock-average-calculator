from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def stock_calculator(request):
    context = {}
    if request.method == "POST":
        qty_on_hand = request.POST.get("qty_on_hand")
        avg_price = request.POST.get("avg_price")
        new_qty = request.POST.get("new_qty")
        new_price = request.POST.get("new_price")
        if qty_on_hand and avg_price and new_qty and new_price:
            total_old_value = float(qty_on_hand) * float(avg_price)
            total_new_value = float(new_qty) * float(new_price)
            total_qty = float(qty_on_hand) + float(new_qty)
            
            context['result'] = (total_old_value + total_new_value) / total_qty
            
        # Add the inputs back into the context so the form can remember them
        context.update({
            'qty_on_hand': qty_on_hand,
            'avg_price': avg_price,
            'new_qty': new_qty,
            'new_price': new_price,
        })
    return render(request, 'calculator.html', context)