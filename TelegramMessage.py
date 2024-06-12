from telethon.sync import TelegramClient
import schedule
import asyncio

# Your Telegram API credentials
api_id = '28730242'
api_hash = '30d531482a4779b6e054c5b9f540270b'
phone_number = '+60142460399'

async def send_message_to_group(client, chat_entity, message):
    try:
        # Send the message to the specified group chat
        await client.send_message(chat_entity, message)
        print("Message sent successfully!")
    except Exception as e:
        print("An error occurred:", e)

async def get_entity_and_send_message(client, group_id, message):
    try:
        # Get the entity of the specified group chat
        entity = await client.get_entity(group_id)
        
        # Send the message to the group chat
        await send_message_to_group(client, entity, message)
    except ValueError as e:
        print("Entity not found:", e)
    except Exception as e:
        print("An error occurred:", e)

async def main():
    try:
        # Initialize the Telegram client
        client = TelegramClient('session_name', api_id, api_hash)
        
        # Connect to Telegram
        await client.start(phone_number)
        
        # Replace 'your_group_name' with the name of your group chat
        # group_name = '维'
        group_id = -4170590641
        
        # The message you want to send
        message = "早上好"
        
        # Run the function to get the entity and send the message to the group
        await get_entity_and_send_message(client, group_id, message)
    except Exception as e:
        print("An error occurred:", e)
    finally:
        # Disconnect from Telegram
        await client.disconnect()

schedule.every().day.at("09:00").do(asyncio.run, main)

# Run the scheduled tasks
while True:
    schedule.run_pending()
    asyncio.sleep(60)  # Check every minute if there's a scheduled task to run