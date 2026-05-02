const BASE_URL = "http://127.0.0.1:5000";

// Load everything
$(document).ready(function () {
    loadServices();
    loadProviders();

    $("#addService").click(createService);
    $("#saveProvider").click(saveProvider);
    $("#serviceFilter").change(filterProviders);
});

// ---------- SERVICES ----------

function loadServices() {
    $.ajax({
        url: BASE_URL + "/services",
        method: "GET",
        success: function (services) {
            $("#serviceList").empty();
            $("#serviceSelect").empty();
            $("#serviceFilter").empty().append('<option value="">All Services</option>');

            services.forEach(s => {
                $("#serviceList").append(`<li>${s.name}</li>`);
                $("#serviceSelect").append(`<option value="${s.id}">${s.name}</option>`);
                $("#serviceFilter").append(`<option value="${s.id}">${s.name}</option>`);
            });
        }
    });
}

function createService() {
    const name = $("#serviceName").val();

    $.ajax({
        url: BASE_URL + "/services",
        method: "POST",
        contentType: "application/json",
        data: JSON.stringify({ name }),
        success: function () {
            loadServices();
            $("#serviceName").val("");
        }
    });
}

// ---------- PROVIDERS ----------

function loadProviders() {
    $.ajax({
        url: BASE_URL + "/providers",
        method: "GET",
        success: renderProviders
    });
}

function filterProviders() {
    const serviceId = $(this).val();

    if (!serviceId) {
        loadProviders();
        return;
    }

    $.ajax({
        url: BASE_URL + "/providers/service/" + serviceId,
        method: "GET",
        success: renderProviders
    });
}

function renderProviders(providers) {
    const tbody = $("#providerTable tbody");
    tbody.empty();

    providers.forEach(p => {
        tbody.append(`
            <tr>
                <td>${p.name}</td>
                <td>${p.email}</td>
                <td>${p.phone}</td>
                <td>${p.price_per_hour}</td>
                <td>${p.service_name}</td>
                <td>
                    <button onclick="editProvider(${p.id})">Edit</button>
                    <button onclick="deleteProvider(${p.id})">Delete</button>
                </td>
            </tr>
        `);
    });
}

function saveProvider() {
    const id = $("#providerId").val();

    const provider = {
        name: $("#name").val(),
        email: $("#email").val(),
        phone: $("#phone").val(),
        price_per_hour: parseFloat($("#rate").val()),
        service_id: parseInt($("#serviceSelect").val())
    };

    if (id) {
        // UPDATE
        $.ajax({
            url: BASE_URL + "/providers/" + id,
            method: "PUT",
            contentType: "application/json",
            data: JSON.stringify(provider),
            success: function () {
                loadProviders();
                clearForm();
            }
        });
    } else {
        // CREATE
        $.ajax({
            url: BASE_URL + "/providers",
            method: "POST",
            contentType: "application/json",
            data: JSON.stringify(provider),
            success: function () {
                loadProviders();
                clearForm();
            }
        });
    }
}

function editProvider(id) {
    $.ajax({
        url: BASE_URL + "/providers/" + id,
        method: "GET",
        success: function (p) {
            $("#providerId").val(p.id);
            $("#name").val(p.name);
            $("#email").val(p.email);
            $("#phone").val(p.phone);
            $("#rate").val(p.price_per_hour);
            $("#serviceSelect").val(p.service_id);
        }
    });
}

function deleteProvider(id) {
    $.ajax({
        url: BASE_URL + "/providers/" + id,
        method: "DELETE",
        success: function () {
            loadProviders();
        }
    });
}

function clearForm() {
    $("#providerId").val("");
    $("#name").val("");
    $("#email").val("");
    $("#phone").val("");
    $("#rate").val("");
}