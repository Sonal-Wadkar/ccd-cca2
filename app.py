
from flask import Flask, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Little Bloom Cafe</title>

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            scroll-behavior: smooth;
        }

        body {
            font-family: Arial, sans-serif;
            background-color: #FFFDF7;
            color: #182747;
        }

        nav {
            background: #182747;
            color: white;
            padding: 20px 8%;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        nav h2 {
            color: #FFE699;
        }

        nav a {
            color: white;
            text-decoration: none;
            margin-left: 20px;
        }

        .hero {
            text-align: center;
            padding: 90px 20px;
            background: #FFE699;
        }

        .hero h1 {
            font-size: 48px;
            margin-bottom: 15px;
        }

        .hero p {
            font-size: 18px;
            margin-bottom: 25px;
        }

        .btn {
            display: inline-block;
            background: #EFA6B8;
            color: #182747;
            padding: 13px 25px;
            border-radius: 25px;
            text-decoration: none;
            font-weight: bold;
        }

        section {
            padding: 55px 8%;
            text-align: center;
        }

        section h2 {
            font-size: 30px;
            margin-bottom: 25px;
        }

        .menu {
            display: flex;
            justify-content: center;
            gap: 20px;
            flex-wrap: wrap;
        }

        .card {
            background: white;
            border: 2px solid #F4D4DC;
            border-radius: 15px;
            padding: 25px;
            width: 220px;
            box-shadow: 0 4px 10px #18274710;
        }

        .card .emoji {
            font-size: 40px;
            margin-bottom: 10px;
        }

        .card h3 {
            margin-bottom: 10px;
        }

        .price {
            color: #B64F72;
            font-weight: bold;
            margin-top: 12px;
        }

        .about {
            background: #FBE6EC;
            line-height: 1.8;
        }

        .contact {
            background: #FFFDF7;
            line-height: 2;
        }

        footer {
            background: #182747;
            color: white;
            text-align: center;
            padding: 20px;
        }

        @media (max-width: 600px) {
            nav {
                flex-direction: column;
                gap: 15px;
            }

            nav a {
                margin: 0 7px;
            }

            .hero h1 {
                font-size: 34px;
            }
        }
    </style>
</head>

<body>

    <nav>
        <h2>🌸 Little Bloom Cafe</h2>
        <div>
            <a href="#home">Home</a>
            <a href="#menu">Menu</a>
            <a href="#about">About</a>
            <a href="#contact">Contact</a>
        </div>
    </nav>

    <div class="hero" id="home">
        <h1>A Little Cup of Happiness ☕</h1>
        <p>Fresh coffee, sweet treats, and cozy moments.</p>
        <p>Now opening at new locations over New York! </p>
        <a href="#menu" class="btn">Explore Our Menu</a>
    </div>

    <section id="menu">
        <h2>Our Favorites 💗</h2>

        <div class="menu">
            <div class="card">
                <div class="emoji">☕</div>
                <h3>Cappuccino</h3>
                <p>Rich coffee with creamy foam.</p>
                <p class="price">₹149</p>
            </div>

            <div class="card">
                <div class="emoji">🍰</div>
                <h3>Strawberry Cake</h3>
                <p>Soft cake with sweet strawberries.</p>
                <p class="price">₹199</p>
            </div>

            <div class="card">
                <div class="emoji">🥪</div>
                <h3>Cheese Sandwich</h3>
                <p>Toasted, cheesy, and delicious.</p>
                <p class="price">₹129</p>
            </div>

            <div class="card">
                <div class="emoji">🍵</div>
                <h3>Pink Rose Latte</h3>
                <p>A floral latte made for cozy days.</p>
                <p class="price">₹179</p>
            </div>
        </div>
    </section>

    <section class="about" id="about">
        <h2>Our Little Story 🌷</h2>
        <p>
            Little Bloom Cafe is a cozy corner for coffee lovers,
            book readers, and dreamers. Come for the coffee,
            stay for the comfort!
        </p>
    </section>

    <section class="contact" id="contact">
        <h2>Come Say Hello!</h2>
        <p>📍 Pune, Maharashtra</p>
        <p>🕒 Monday – Sunday: 9 AM – 9 PM</p>
        <p>💌 hello@littlebloomcafe.com</p>
    </section>

    <footer>
        <p>© 2026 Little Bloom Cafe | Made with ☕ and love</p>
    </footer>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
