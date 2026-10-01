import requests, random, datetime, os, argparse

TOPICS = [
    "Top 5 AI Tools to Grow Your Business in 2026 - AIHubGlobal.com",
    "How AI is Changing Digital Marketing - Learn at AIHubGlobal.com",
    "ChatGPT vs Gemini vs Claude - Which is Best? AIHubGlobal.com",
    "Make Money with AI - 3 Secret Methods - AIHubGlobal.com",
    "AI for Students - Study 10x Faster - AIHubGlobal.com",
    "Future of AI in India - Aurangabad Businesses - AIHubGlobal.com",
    "How to Automate Your Instagram with AI - AIHubGlobal.com",
    "AI Video Creation - No Face Needed - AIHubGlobal.com",
    "Best AI Tools for Content Creators - AIHubGlobal.com",
    "AIHubGlobal.com - Your Complete AI Learning Platform"
]

HASHTAGS = "\n\n#AI #ArtificialIntelligence #AIHubGlobal #ChatGPT #AITips #DigitalMarketing #AIAutomation #Aurangabad #BusinessGrowth #AITools"

def get_post():
    today = datetime.date.today().day
    topic = TOPICS[today % len(TOPICS)]
    text = f"🚀 {topic}{HASHTAGS}\n\n👉 Visit: https://AIHubGlobal.com"
    return text

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--platforms', nargs='+', default=["instagram","facebook","linkedin","threads"])
    parser.add_argument('--publish', action='store_true')
    args = parser.parse_args()
    
    post_text = get_post()
    print(f"Posting: {post_text}")

    if args.publish:
        api_key = os.getenv("AYRSHARE_API_KEY")
        if not api_key:
            print("AYRSHARE_API_KEY missing")
            return
        
        url = "https://app.ayrshare.com/api/post"
        headers = {"Authorization": f"Bearer {api_key}"}
        payload = {
            "post": post_text,
            "platforms": args.platforms
        }
        r = requests.post(url, json=payload, headers=headers)
        print(r.json())
    else:
        print("Dry run - use --publish to post")

if __name__ == "__main__":
    main()
