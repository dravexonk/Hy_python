from bs4 import BeautifulSoup
import requests
import sys


def scrape_website(url):
  """Website se clean text extract karta hai bina kisi API key ke."""
  try:
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Linux; Android 10; Mobile) AppleWebKit/537.36"
        )
    }
    print(f"\n[*] Connecting to: {url}...")
    response = requests.get(url, headers=headers, timeout=15)

    if response.status_code == 200:
      soup = BeautifulSoup(response.text, "html.parser")

      # Unnecessary elements ko hata dena
      for element in soup(["script", "style", "nav", "footer", "header", "aside"]):
        element.decompose()

      clean_text = soup.get_text(separator="\n", strip=True)
      return clean_text
    else:
      return (
          f"[!] Error: Page fetch nahi ho saka. Status Code:"
          f" {response.status_code}"
      )

  except Exception as e:
    return f"[!] Connection Error: {e}"


def main():
  print("=" * 50)
  print("  Advanced Local Mobile Web Reader (Zero API)")
  print("=" * 50)

  while True:
    url = input(
        "\nKiska data padhna hai? URL daalein (Exit ke liye 'q' dabayein): "
    ).strip()

    if url.lower() == "q":
      print("Program band ho raha hai. Alvida!")
      break

    if not url.startswith("http"):
      url = "https://" + url

    content = scrape_website(url)

    print("\n" + "=" * 20 + " Extracted Content (Preview) " + "=" * 20)
    print(content[:2000])  # Pehle 2000 characters screen par dikhayega
    print("=" * 65)

    # File save karne ka feature
    save_choice = (
        input("\nKya aap is poore content ko file me save karna chahte hain?"
              " (y/n): ")
        .strip()
        .lower()
    )
    if save_choice == "y":
      filename = (
          input("File ka naam likhein (jaise data.txt): ").strip()
          or "scraped_data.txt"
      )
      try:
        with open(filename, "w", encoding="utf-8") as f:
          f.write(content)
        print(f"[+] Success! File '{filename}' aapke phone me save ho gayi hai.")
      except Exception as e:
        print(f"[!] File save karne me error aayi: {e}")


if __name__ == "__main__":
  main()
  
