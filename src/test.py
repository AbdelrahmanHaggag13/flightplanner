from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights
from backend import run_travel_agent

res=run_travel_agent(user_input="plan a 7 days trips to japan from Egypt ", thread_id="test_thread_1")

print(res)



