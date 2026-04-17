from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Deal

# List view for all deals
def deals_list(request):
    now = timezone.now()
    deals = Deal.objects.filter(is_active=True, start_date__lte=now).order_by('-created_at')
    query = request.GET.get('q', '')
    if query:
        deals = deals.filter(title__icontains=query)
    return render(request, 'deals/deals.html', {'deals': deals, 'query': query})

# Detail view for a single deal
def deal_detail(request, pk):
    deal = get_object_or_404(Deal, pk=pk, is_active=True, start_date__lte=timezone.now())
    return render(request, 'deals/deal_detail.html', {'deal': deal})
