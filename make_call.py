import pjsua as pj

# Logging callback to display errors
def log_cb(level, str, len):
    print(str),

# Initializing the library
pj.Lib.instance().init(log_cfg = pj.LogConfig(level=3, callback=log_cb))

# Creating a library instance
lib = pj.Lib()

try:
    # Creating UDP transport
    transport = lib.create_transport(pj.TransportType.UDP)

    # Starting the library (initializing library)
    lib.start()

    # Creating SIP account
    acc = lib.create_account(pj.AccountConfig(
        'sip:your_username@your_sip_provider.com',  # Replace with your SIP account details
        'your_password'
    ))

    # Making a call
    call = acc.make_call('7892098558')  # Replace with the phone number to call

    # Wait for the call to be answered
    while True:
        pj.Wait(0.5)

except pj.Error as e:
    print("Exception: " + str(e))
    call = None

# Shutdown the library
lib.destroy()
lib = None
