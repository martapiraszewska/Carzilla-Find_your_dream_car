from flask import Blueprint, request, jsonify
from ..models import Employee
from typing import List
from ..cars.routes import search_car

main_bp = Blueprint("main", __name__)

# i can test all endpoints in employee route, cars and main.search_cars
# and of course validation


# @main_bp.route("/search", methods=["GET"])
# def search_cars():
#     # Example: /search?brand=Toyota&model=Corolla
#     return search_car(request.args)


# @main_bp.route("/employees", methods=["GET"])
# def manage_employees():
#     if request.method == "GET":
#         employees: List[Employee] = Employee.query.all()
#         return jsonify(
#             [
#                 {
#                     "id": employee.Employee_ID,
#                     "name": f"{employee.Name} {employee.Surname}",
#                 }
#                 for employee in employees
#             ]
#         )


@main_bp.route("/", methods=["GET"])
def main_page():
    return """
    <!DOCTYPE html>
    <html lang="pl">
    <head>
        <meta charset="UTF-8">
        <title>REST API Tester</title>
        <style>
            body { font-family: Arial, sans-serif; padding: 20px; max-width: 700px; margin: auto; }
            label { display: block; margin-top: 10px; }
            input, select, textarea { width: 100%; padding: 8px; margin-top: 4px; }
            button { margin-top: 15px; padding: 10px 20px; }
            pre { background: #f4f4f4; padding: 10px; white-space: pre-wrap; border: 1px solid #ccc; }
        </style>
    </head>
    <body>

    <h1>REST API Tester</h1>

    <form id="apiForm">
        <label>
            Endpoint:
            <select id="endpoint">
                <option value="/employees">/employees</option>
                <option value="/cars">/cars</option>
            </select>
        </label>

        <label>
            Metoda:
            <select id="method">
                <option value="GET">GET</option>
                <option value="POST">POST</option>
                <option value="PUT">PUT</option>
                <option value="DELETE">DELETE</option>
            </select>
        </label>

        <label>
            ID zasobu (opcjonalne):
            <input type="text" id="resourceId" placeholder="np. 1">
        </label>

        <label>
            Dane (klucz=wartość, rozdzielone enterem):
            <textarea id="formData" placeholder="name=Jan&#10;position=Driver"></textarea>
        </label>

        <button type="submit">Wyślij żądanie</button>
    </form>

    <h2>Odpowiedź serwera:</h2>
    <pre id="responseOutput">Brak danych</pre>

    <script>
        document.getElementById('apiForm').addEventListener('submit', async function (e) {
            e.preventDefault();

            const endpoint = document.getElementById('endpoint').value;
            const method = document.getElementById('method').value;
            const id = document.getElementById('resourceId').value.trim();
            const formDataRaw = document.getElementById('formData').value.trim();

            let url = id ? `${endpoint}/${id}` : endpoint;
            let options = { method: method };

            let data = null;

            if (formDataRaw) {
                const formData = {};
                formDataRaw.split(`\n`).forEach(line => {
                    const [key, value] = line.split('=');
                    if (key && value !== undefined) {
                        formData[key.trim()] = value.trim();
                    }
                });

                if (method === 'POST' || method === 'PUT') {
                    // Przygotowanie danych do wysłania w formacie JSON dla POST/PUT
                    options.headers = { 'Content-Type': 'application/json' };
                    options.body = JSON.stringify(formData);
                } else if (method === 'GET' || method === 'DELETE') {
                    // Przygotowanie zapytania z parametrami URL dla GET/DELETE
                    const query = new URLSearchParams(formData).toString();
                    if (query) {
                        url += `?${query}`;
                    }
                }
            }

            try {
                console.log("Finalny URL:", url);
                console.log("Opcje:", options);
                const response = await fetch(url, options);
                const contentType = response.headers.get('Content-Type') || '';
                let text;
                if (contentType.includes('application/json')) {
                    const json = await response.json();
                    text = JSON.stringify(json, null, 2);
                } else {
                    text = await response.text();
                }

                document.getElementById('responseOutput').textContent =
                    `Status: ${response.status} ${response.statusText}\n\n${text}`;
            } catch (error) {
                document.getElementById('responseOutput').textContent = 'Błąd sieci: ' + error;
            }
        });
    </script>

    </body>
    </html>




    """


# @main_bp.route("/", methods=["GET"])
# def main_page():
#     return """
#     <!DOCTYPE html>
#     <html lang="en">
#     <head>
#         <meta charset="UTF-8">
#         <meta name="viewport" content="width=device-width, initial-scale=1.0">
#         <title>Flask Button with Script</title>
#     </head>
#     <body>
#         <button onclick="sendLoginRequest('admin')">LoginAdmin</button>
#         <button onclick="sendLoginRequest('worker1')">Login</button>

#         <script>
#             function sendLoginRequest(login_) {
#                 fetch('http://127.0.0.1:5000/auth/login', {
#                     method: 'POST',
#                     headers: {
#                         'Content-Type': 'application/json'  // Ensure the correct content type
#                     },
#                     body: JSON.stringify({
#                         login: login_,
#                         password: 'temp'
#                     })
#                 })
#                 .then(response => {
#                     if (response.redirected) {
#                         window.location.href = response.url;  // This will redirect the browser to the new URL
#                     } else {
#                         return response.json();  // Handle the case where no redirect occurs
#                     }
#                 })
#                 .then(data => {
#                     console.log(data);  // This will handle any JSON data you may want to log
#                 })
#                 .catch(error => console.error('Error:', error));
#             }
#         </script>
#     </body>
#     </html>
#     """
