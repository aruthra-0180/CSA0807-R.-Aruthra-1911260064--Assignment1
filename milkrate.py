BASE_RATE = 30.00
FAT_STEP = 0.40
SNF_STEP = 0.30


def rate_per_litre(fat, snf):
    fat_steps = round((fat - 3.5) * 10)
    snf_steps = round((snf - 8.5) * 10)

    rate = BASE_RATE + fat_steps * FAT_STEP + snf_steps * SNF_STEP
    return round(rate, 2)


def payout(litres, fat, snf):
    rate = rate_per_litre(fat, snf)
    return round(litres * rate, 2)