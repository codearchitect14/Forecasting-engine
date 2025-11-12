#!/usr/bin/env python3
"""
Quick performance test for the optimized demand/inventory endpoint
"""
import requests
import time
import json

def test_5x5x5():
    """Test 5x5x5 combinations"""
    url = "http://127.0.0.1:7000/api/demand-forecast"

    payload = {
        "city_ids": ["1", "2", "3", "4", "5"],
        "store_ids": ["1", "2", "3", "4", "5"],
        "product_ids": [1, 2, 3, 4, 5],
        "forecast_days": 30
    }

    print(f"🚀 Testing {len(payload['city_ids'])}×{len(payload['store_ids'])}×{len(payload['product_ids'])} = {len(payload['city_ids']) * len(payload['store_ids']) * len(payload['product_ids'])} combinations")
    print("📊 Target: <10 seconds"
    print("-" * 50)

    start_time = time.time()

    try:
        print("⏳ Sending request...")
        response = requests.post(url, json=payload, timeout=300)  # 5 minute timeout

        end_time = time.time()
        total_time = end_time - start_time

        print(".3f"
        print(f"📊 Status: {response.status_code}")

        if response.status_code == 200:
            data = response.json()
            print("✅ SUCCESS!")
            print(f"📦 Response size: {len(json.dumps(data))} characters")
            print(f"🔢 Demand forecasts: {len(data.get('demand_forecasts', {}))}")
            print(f"📋 Insights: {len(data.get('demand_insights', []))}")
            print(f"💡 Recommendations: {len(data.get('inventory_recommendations', []))}")

            if total_time < 10:
                print("🎉 TARGET ACHIEVED! Under 10 seconds!"            else:
                print(f"⚠️  Still over target, but much better than 242s!")
        else:
            print(f"❌ FAILED: {response.status_code}")
            print(f"Error: {response.text}")

    except requests.exceptions.Timeout:
        print("⏰ TIMEOUT: Request took longer than 5 minutes")
    except Exception as e:
        print(f"💥 ERROR: {e}")

if __name__ == "__main__":
    test_5x5x5()

