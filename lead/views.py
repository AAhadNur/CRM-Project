from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse

from .forms import AddLeadForm
from .models import Lead


@login_required
def leads_list(request):
    leads = Lead.objects.filter(created_by=request.user)

    context = {'leads': leads}
    return render(request, 'lead/leads_list.html', context)


@login_required
def lead_detail(request, pk):
    lead = Lead.objects.filter(created_by=request.user).get(id=pk)

    context = {'lead': lead}
    return render(request, 'lead/lead_detail.html', context)


@login_required
def add_leads(request):
    if request.method == "POST":
        form = AddLeadForm(request.POST)

        if form.is_valid():
            lead = form.save(commit=False)
            lead.created_by = request.user
            lead.save()
            messages.success(request, 'The was created successfully!!!')

            return redirect('leads_list')

    else:
        form = AddLeadForm()

    context = {'form': form}

    return render(request, 'lead/add_lead.html', context)


@login_required
def edit_lead(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, id=pk)

    if request.method == "POST":
        form = AddLeadForm(request.POST, instance=lead)

        if form.is_valid():
            form.save()

            messages.success(request, 'The changes was saved.')

            return redirect('leads_list')

    else:
        form = AddLeadForm(instance=lead)

    context = {'form': form}

    return render(request, 'lead/edit_lead.html', context)


@login_required
def lead_delete(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, id=pk)

    if lead.created_by != request.user:
        return HttpResponse('You are not allowed here')

    if request.method == "POST":
        lead.delete()
        messages.success(request, 'The lead was deleted successfully!!!')
        return redirect('leads_list')

    context = {'lead': lead}

    return render(request, 'lead/lead_delete.html', context)
