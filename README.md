Step 18 – SQLAlchemy ORM
===================

💭 Problem / Pain
-----------------
Data isn't being saved to database.
POST endpoint only returns "Saved" message.

🛠️ Tasks
--------
- Fix data persistence issue
- Improve POST response with created data

✅ Check
--------
1. Reset database:
   - Stop and remove: `docker compose down -v`
   - Start fresh: `docker compose up -d`
   - Check tables: `docker exec health-db psql -U healthuser -d healthdb -c "\dt"`

2. Start app:
   - Run: `uvicorn main:app --reload`
   - Check tables again - they exist!
   - Look at main.py to see how

3. Test saving:
   - Add new observation
   - List observations - all empty!
   - Fix persistence
   - Data shows up in list

4. Test response:
   - Add another observation
   - Check response has full data
   - Not just "Saved" message
