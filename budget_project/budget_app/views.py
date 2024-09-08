import re
from urllib import request
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST


# Create your views here.
def index(request):
    entries = request.session.get("entries", [])
    total_income = sum(
        entry["amount"] for entry in entries if entry["type"] == "income"
    )
    total_expenses = sum(
        entry["amount"] for entry in entries if entry["type"] == "expense"
    )
    balance = total_income - total_expenses

    context = {
        "balance": balance,
        "entries": entries,
        "total_income": total_income,
        "total_expenses": total_expenses,
    }
    return render(request, "budget_app/index.html", context)


def add_entry(request):
    if request.method == "POST":
        entry_type = request.POST.get("type")
        amount = float(request.POST.get("amount"))
        description = request.POST.get("description")

        entries = request.session.get("entries", [])
        entries.append(
            {"type": entry_type, "amount": amount, "description": description}
        )
        request.session["entries"] = entries

        return redirect("index")

    return render(request, "budget_app/add_entry.html")


def edit_entry(request, id):
    entries = request.session.get("entries", [])
    entry = entries[id]

    if request.method == "POST":
        entry["type"] = request.POST.get("type")
        entry["amount"] = float(request.POST.get("amount"))
        entry["description"] = request.POST.get("description")

        request.session["entries"] = entries
        return redirect("index")

    context = {"entry": entry, "id": id}

    return render(request, "budget_app/edit_entry.html", context)


@require_POST
def delete_entry(request, id):
    entries = request.session.get("entries", [])
    entries.pop(id)
    request.session["entries"] = entries
    return redirect("index")

def track_visits(request):
    visit_count = request.session.get('visit_count', 1)

