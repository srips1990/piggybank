
var ajaxTransactionRequest = function(endpoint, method, params, status_elem, status_func, _invoker=undefined) {
	var xmlhttp = new XMLHttpRequest();
    console.log(_invoker);
	if(_invoker)
        _invoker.disabled = true;
    var headers = {
        "X-CSRFToken": document.getElementsByName('csrfmiddlewaretoken')[0].value
    }

	try {

		xmlhttp.onreadystatechange = function () {

			if (xmlhttp.readyState == 4) {
			    if(_invoker)
			        _invoker.disabled = false;
//                status_elem.innerHTML = "";

				if(xmlhttp.status == 200) {
				    var resp_json = JSON.parse(xmlhttp.responseText);
				    status_elem.style.color = 'green';
				    status_elem.innerHTML = status_func(resp_json);
				}
				else if (xmlhttp.status == 500) {
					console.log(xmlhttp);
                    error_msg = xmlhttp.responseText;
				    status_elem.style.color = 'red';
                    status_elem.innerHTML = error_msg;
				}
			}
		};

		xmlhttp.open(method, endpoint, true);       // Initializing xmlhttp object to the desired endpoint
		// Setting headers
		for(header_name in headers) {
		    xmlhttp.setRequestHeader(header_name, headers[header_name]);
		}
        // Setting form data
		var formData = new FormData();
		for(param_name in params) {
            formData.append(param_name, params[param_name]);
		}

		xmlhttp.send(formData);     // Sending HTTP request
	}
	catch (e) {
		console.log("Error: " + xmlhttp.statusText + e.description);
	}
}

var prepareTransactionStatus = function(resp_json) {
    return "Transaction Hash: &ensp;" + resp_json.txReceipt.transactionHash;
}

var prepareBalanceStatus = function(resp_json) {
    return resp_json.balance;
}

var prepareAllowanceStatus = function(resp_json) {
    return resp_json.allowance;
}

var getAccountBalance = function(from_addr) {
    var params = {
        "from_addr": from_addr.value
    }
    var status_elem = document.getElementById("balance");
	try {
		ajaxTransactionRequest("get_balance", "POST", params, status_elem, prepareBalanceStatus);
	}
	catch (e) {
		console.log(e.description);
	}
}

var getContractBalance = function() {
    var params = {
    }
    var status_elem = document.getElementById("contract_balance");
	try {
		ajaxTransactionRequest("get_contract_balance", "GET", params, status_elem, prepareBalanceStatus);
	}
	catch (e) {
		console.log(e.description);
	}
}

var deposit = function(deposit_from_addr, deposit_qty, invoker) {
    var params = {
        "deposit_from_addr": deposit_from_addr.value,
        "deposit_qty": deposit_qty.value
    }
    var status_elem = document.getElementById("deposit_status");
    status_elem.innerHTML = "<b><i>Processing...</i></b>";
	try {
		ajaxTransactionRequest("deposit", "POST", params, status_elem, prepareTransactionStatus, invoker);
	}
	catch (e) {
		console.log(e.description);
	}
}

var grantAllowance = function(grant_from_addr, grant_to_addr, grant_qty, invoker) {
    var params = {
        "grant_from_addr": grant_from_addr.value,
        "grant_to_addr": grant_to_addr.value,
        "grant_qty": grant_qty.value
    }
    var status_elem = document.getElementById("grant_status");
    status_elem.innerHTML = "<b><i>Processing...</i></b>";
	try {
		ajaxTransactionRequest("grant_allowance", "POST", params, status_elem, prepareTransactionStatus, invoker);
	}
	catch (e) {
		console.log(e.description);
	}
}

var withdraw = function(withdraw_addr, withdraw_qty, invoker) {
    var params = {
        "withdraw_addr": withdraw_addr.value,
        "withdraw_qty": withdraw_qty.value
    }
    var status_elem = document.getElementById("withdraw_status");
    status_elem.innerHTML = "<b><i>Processing...</i></b>";

	try {
		ajaxTransactionRequest("withdraw", "POST", params, status_elem, prepareTransactionStatus, invoker);
	}
	catch (e) {
		console.log(e.description);
	}
}

var getAllowance = function(user_addr) {
    var params = {
        "user_addr": user_addr.value
    }
    var status_elem = document.getElementById("user_allowance");

	try {
		ajaxTransactionRequest("get_allowance", "POST", params, status_elem, prepareAllowanceStatus);
	}
	catch (e) {
		console.log(e.description);
	}
}
