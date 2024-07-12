!curl -F 'name=cloud-colored-image' -F 'file=@/home/jack/Desktop/LBRY-cli/videos-complete/junk1/cloud-colored-image.png' https://spee.ch/api/claim/publish

import urllib, json
import requests
requests.post("http://localhost:5279", json={"method": "publish", "params": {"name": "cloud-colored-image","bid": "0.15", "file_path": "/home/jack/Desktop/LBRY-cli/VIDEOS/Clouds-Palette-Colors-Sound.mp4", "tags": "art","tags":"digital graphics", "tags":"gimp images", "languages": "en", "locations": "PH", "channel_name":"@MyLinuxToyBox","thumbnail_url":"https://spee.ch/2/cloud-colored-image"}}).json()


"claim_id": "f0e1ccae16cc1160cbfb028034d5176c98b3dd16",  MyLinuxToyBox

!curl -F 'name=Palette-Swapped-Image' -F 'file=@/mnt/40ec525c-34bc-44ef-99c8-53f5524ad88b/Images/Pallet-swapped/07a-Thum.jpg' https://spee.ch/api/claim/publish
----------------------------------------------------------------------------------------------------------------
{"success":true,"message":"publish completed successfully","data":{"name":"Palette-Swapped-Image","claimId":"e7c2e060400eebddbfca70c67e44ee776078c0ef","url":"https://spee.ch/e/Palette-Swapped-Image","showUrl":"https://spee.ch/e/Palette-Swapped-Image","serveUrl":"https://spee.ch/e/Palette-Swapped-Image.jpg","pushTo":"/e/Palette-Swapped-Image","claimData":{"name":"Palette-Swapped-Image","claimId":"e7c2e060400eebddbfca70c67e44ee776078c0ef","title":"Palette-Swapped-Image","description":"","address":"bFFR9aqXaamuihY8mowejqHWHgyjktx2nm","outpoint":"483ccccf2e8204e83fea4973ca137684050bbc721ce0669fa3bd2c39110b0af6:0","height":475584,"contentType":"image/jpeg","amount":"0.01","certificateId":null,"channelName":null}}}

import urllib, json
import requests
requests.post("http://localhost:5279", json={"method": "publish", "params": {"name": "Palette-Swapped-Image","bid": "0.15", "file_path": "/mnt/40ec525c-34bc-44ef-99c8-53f5524ad88b/Images/Pallet-swapped/07a.jpg", "tags": "art_digital graphics_gimp images", "languages": "en", "locations": "PH", "channel_account_id": "@MyLinuxToyBox","thumbnail_url":"https://spee.ch/e/Palette-Swapped-Image.jpg"}}).json()

import urllib, json
import requests
IMAGE = "/mnt/40ec525c-34bc-44ef-99c8-53f5524ad88b/Images/ART-blended/blended20190407203210.jpg"
requests.post("http://localhost:5279", json={"method": "publish", "params": {"name": "First Bot Post","bid": "0.15", "file_path": IMAGE, "tags": "art,digital graphics,images", "languages": "en", "locations": "PH", "channel_account_id": "@MyLinuxToyBox","thumbnail_url":"https://spee.ch/c/blended-thumb"}}).json()

import urllib, json
import requests
IMAGE = "/mnt/40ec525c-34bc-44ef-99c8-53f5524ad88b/Images/ART-blended/blended20190407203210.jpg"
requests.post("http://localhost:5279", json={"method": "publish", "params": {"name": "FirstBotPost001","bid": ".5", "file_path": IMAGE, "tags": "art,digital graphics,images", "languages": "en", "locations": "PH", "channel_account_id": "@MyLinuxToyBox","funding_account_ids": ,"thumbnail_url":"https://spee.ch/c/blended-thumb"}}).json()

import urllib, json
import requests
requests.post("http://localhost:5279", json={"method": "publish", "params": {"name": "Blended Images", "bid": "0.2", "file_path": "/mnt/40ec525c-34bc-44ef-99c8-53f5524ad88b/Images/ART-blended/blended20190407203210.jpg", "tags": "graphic art image", "languages": "en", "locations": "PH","title":"Blended Image" ,"channel_account_id": "@MyLinuxToyBox","thumbnail_url":"https://spee.ch/c/blended-thumb","preview": "false", "blocking": "false"}}).json()

import urllib, json
import requests
requests.post("http://localhost:5279", json={"method": "publish", "params": {"name": "Blended Images", "bid": "0.2", "file_path": "/mnt/40ec525c-34bc-44ef-99c8-53f5524ad88b/Images/ART-blended/blended20190407203210.jpg", "tags": "art, test post, graphic image ", "languages": "en", "locations": "PH","title":"Blended Image" ,"channel_account_id": "@MyLinuxToyBox","thumbnail_url":"https://spee.ch/c/blended-thumb", "funding_account_ids": "PhilippineRetirement", "preview": "false", "blocking": "false"}}).json()

/mnt/40ec525c-34bc-44ef-99c8-53f5524ad88b/Images/ART-blended/blended20190407203210.gif
https://spee.ch/c/blended-thumb
<img alt="blended-thumb" src="https://spee.ch/c/blended-thumb.gif" />
blended-thumb#cb0fee9808bca38d405482c671330df754ea4822
https://open.lbry.com/blended-thumb#cb0fee9808bca38d405482c671330df754ea4822
    
https://open.lbry.com/@MyLinuxToyBox#f
MyLinuxToyBox
@MyLinuxToyBox

@elcer

!lbrynet publish --name=Posted CLI image --bid=0.2 --file_path=/mnt/40ec525c-34bc-44ef-99c8-53f5524ad88b/Images/ART-blended/blended20190407203210.jpg --description=Testing the description out --title=IMAGE-TEST-OO2 --thumbnail_url=https://spee.ch/c/blended-thumb --tags=art videos graphics --channel_account_id=@DigitalArt

from hiddenID import funding
ss=funding()
print ss

!lbrynet publish --name=Test-Image --bid=0.5 --file_path=/mnt/40ec525c-34bc-44ef-99c8-53f5524ad88b/Images/ART-blended/blended20190407203210.jpg --title=IMAGE-TEST-two --channel_account_id=@DigitalArt

!lbrynet resolve Test-Image


    name
    str
    name of the content (can only consist of a-z A-Z 0-9 and -(dash))
    bid
    optionaldecimal
    amount to back the claim
    file_path
    optionalstr
    path to file to be associated with name.
    fee_currency
    optionalstring
    specify fee currency
    fee_amount
    optionaldecimal
    content download fee
    fee_address
    optionalstr
    address where to send fee payments, will use value from --claim_address if not provided
    title
    optionalstr
    title of the publication
    description
    optionalstr
    description of the publication
    author
    optionalstr
    author of the publication. The usage for this field is not the same as for channels. The author field is used to credit an author who is not the publisher and is not represented by the channel. For example, a pdf file of 'The Odyssey' has an author of 'Homer' but may by published to a channel such as '@classics', or to no channel at all
    tags
    optionallist
    add content tags
    languages
    optionallist
    languages used by the channel, using RFC 5646 format, eg: for English `--languages=en` for Spanish (Spain) `--languages=es-ES` for Spanish (Mexican) `--languages=es-MX` for Chinese (Simplified) `--languages=zh-Hans` for Chinese (Traditional) `--languages=zh-Hant`
    locations
    optionallist
    locations relevant to the stream, consisting of 2 letter `country` code and a `state`, `city` and a postal `code` along with a `latitude` and `longitude`. for JSON RPC: pass a dictionary with aforementioned attributes as keys, eg: ... "locations": [{'country': 'US', 'state': 'NH'}] ... for command line: pass a colon delimited list with values in the following order: "COUNTRY:STATE:CITY:CODE:LATITUDE:LONGITUDE" making sure to include colon for blank values, for example to provide only the city: ... --locations="::Manchester" with all values set: ... --locations="US:NH:Manchester:03101:42.990605:-71.460989" optionally, you can just pass the "LATITUDE:LONGITUDE": ... --locations="42.990605:-71.460989" finally, you can also pass JSON string of dictionary on the command line as you would via JSON RPC ... --locations="{'country': 'US', 'state': 'NH'}"
    license
    optionalstr
    publication license
    license_url
    optionalstr
    publication license url
    thumbnail_url
    optionalstr
    thumbnail url
    release_time
    optionalint
    original public release of content, seconds since UNIX epoch
    width
    optionalint
    image/video width, automatically calculated from media file
    height
    optionalint
    image/video height, automatically calculated from media file
    duration
    optionalint
    audio/video duration in seconds, automatically calculated
    channel_id
    optionalstr
    claim id of the publisher channel
    channel_name
    optionalstr
    name of publisher channel
    channel_account_id
    optionalstr
    one or more account ids for accounts to look in for channel certificates, defaults to all accounts.
    account_id
    optionalstr
    account to use for holding the transaction
    wallet_id
    optionalstr
    restrict operation to specific wallet
    funding_account_ids
    optionallist
    ids of accounts to fund this transaction
    claim_address
    optionalstr
    address where the claim is sent to, if not specified it will be determined automatically from the account
    preview
    optionalbool
    do not broadcast the transaction
    blocking
    optionalbool
    wait until transaction is in mempool


link lbry://blended-thumb#c

(base) jack@server1:~/lighthouse$ lbrynet resolve lbry://blended-thumb#c
{
  "lbry://blended-thumb#c": {
    "address": "bFFR9aqXaamuihY8mowejqHWHgyjktx2nm",
    "amount": "0.01",
    "canonical_url": "lbry://blended-thumb#c",
    "claim_id": "cb0fee9808bca38d405482c671330df754ea4822",
    "claim_op": "create",
    "confirmations": 55,
    "height": 696816,
    "meta": {
      "activation_height": 696816,
      "creation_height": 696816,
      "creation_timestamp": 1578620921,
      "effective_amount": "0.01",
      "expiration_height": 2799216,
      "is_controlling": true,
      "reposted": 0,
      "support_amount": "0.0",
      "take_over_height": 696816,
      "trending_global": 0.0,
      "trending_group": 0,
      "trending_local": 0.0,
      "trending_mixed": 0.0
    },
    "name": "blended-thumb",
    "normalized_name": "blended-thumb",
    "nout": 0,
    "permanent_url": "lbry://blended-thumb#cb0fee9808bca38d405482c671330df754ea4822",
    "short_url": "lbry://blended-thumb#c",
    "timestamp": 1578620921,
    "txid": "64f6d042b9d8f49f3e0640cde9f23a7ea3af860897eccf686639a0baddcb6a2a",
    "type": "claim",
    "value": {
      "author": "Spee.ch",
      "image": {
        "height": 720,
        "width": 1280
      },
      "languages": [
        "en"
      ],
      "source": {
        "hash": "ecf17ea796d7bc09dfc4ec348edb56e8fcbc5f236b049af294cda30bb6dec6d5774054d05232aa87b1ce64e48b586831",
        "media_type": "image/gif",
        "name": "hMP2zHe8APA1xXYus4B_nWR9.gif",
        "sd_hash": "74c46a3a85e91e05b95bd20c67e8d8e1fe77921b1aff95816c6eec2c1ef06a09ae5c8651fe9c20d0cf7e2f0615f614d1",
        "size": "1067432"
      },
      "stream_type": "image",
      "title": "blended-thumb"
    },
    "value_type": "stream"
  }
}


