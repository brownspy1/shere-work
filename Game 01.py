choice = input("তুমি কি আমাদের সাথে যেতে চাও ? [Yes/No]:")
if choice == "Yes" or choice == "yes":
    print("রহস্যময় দ্বীপ এ তোমাকে স্বাগতম !")
    choice = input("তুমি কি ঝর্ণার কাছে যাবে ? [Yes/No]:")
    if choice == "Yes" or choice == "yes":
        choice = input("ঝর্ণার পানিতে নামবে ? [Yes/No]:")
        if choice == "Yes" or choice == "yes":
            print("হায় হায় তুমি তো সাঁতার জানোনা ! you are a loser!")

        else:
            choice = input("ঝর্ণার পাশে বসবে? [Yes/No]")
            if choice == "Yes" or choice == "yes":
                print("ঝর্ণার পাশে সাপ ছিল ! হা হা তুমি হেরে গেলে !")
            else:
                choice = input("তুমি কি ঝর্ণার পাশের গুহায় ঢুকতে চাও? [Yes/No]")
                if choice == "Yes" or choice == "yes":
                    print("চমৎকার তুমি নতুন গুহা আবিষ্কার করে ফেলেছ। তুমি জিতে গেলে !")

    else:
        choice = input(" তুমি কি গাছ তলায় বিশ্রাম নিবে ? [Yes/No]")
        if choice == "Yes" or choice == "yes":
            pass
        else:
            choice = input(" তুমি কি নদীতে সাঁতার কাটবে ? [Yes/No]")
            if choice == "Yes" or choice == "yes":
                pass
            else:
                choice = input("তুমি কি জলপরী দেখবে ? [Yes/no]")
                if choice == "Yes" or choice == "yes":
                    pass
                else:
                    choice = input("  তুমি কি ভাল্লুক দেখবে ? [Yes/No]")
                    if choice == "Yes" or choice == "yes":
                        pass
                    else:
                        choice = input(" তুমি কি বাড়ি যেতে চাও ? [Yes/No]")
                        if choice == "Yes" or choice == "yes":
                            pass
                        else:
                            print(" চলো আমরা আম গাছ থেকে আম পাড়ি !")
                            choice = input("")
else:
    print("তুমি অনেক মজার একটা এডভেঞ্চার মিস করলে !")

