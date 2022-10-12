from discord_webhook import DiscordWebhook, DiscordEmbed
webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1029782883713417226/nx_cBM4YFMrZ7wQmGkZw50NlBd4sBtKsOWTXQKmBMI_wQy-7Pv1omsEf-L1qhKhRJViH')

embed = DiscordEmbed(title='You created a embed with a webhook!', description=f'This is callled a Embed!', color='242424')

webhook.add_embed(embed)

response = webhook.execute()
print(response)
