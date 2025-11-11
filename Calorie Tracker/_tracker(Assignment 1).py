{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b2b9752f-56fa-49b2-9c7f-666b7e913e2d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "--------------------------------------------------\n",
      "       Welcome to the Daily Calorie Tracker!      \n",
      "--------------------------------------------------\n",
      "\n",
      ">This tool helps you to log your meals and track your daily calorie intake.\n",
      ">You can enter your meals, see the total, and compare it with your daily limit.\n",
      "\n",
      "\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "How many meals would you like to log?\n",
      "  2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the name for meal #1:  breakfast\n"
     ]
    }
   ],
   "source": [
    "## Name: Madhav Kalra\n",
    "# Date: 6/11/2025\n",
    "# Project Title: Daily Calorie Tracker CLI\n",
    "\n",
    "import datetime\n",
    "\n",
    "def welcome():\n",
    "    print(\"-\"*50)\n",
    "    print(\"       Welcome to the Daily Calorie Tracker!      \")\n",
    "    print(\"-\"*50)\n",
    "    print(\"\\n>This tool helps you to log your meals and track your daily calorie intake.\")\n",
    "    print(\">You can enter your meals, see the total, and compare it with your daily limit.\\n\\n\")\n",
    "\n",
    "welcome()\n",
    "\n",
    "meal_l=[]\n",
    "cal_l=[]\n",
    "\n",
    "num=int(input(\"How many meals would you like to log?\\n \"))\n",
    "print()\n",
    "\n",
    "for i in range(num):\n",
    "\n",
    "    m_name=input(f\"Enter the name for meal #{i + 1}: \")\n",
    "    cal=float(input(f\"Enter the calories for {m_name}: \"))\n",
    "\n",
    "    meal_l.append(m_name)\n",
    "    cal_l.append(cal)\n",
    "\n",
    "total=sum(cal_l)\n",
    "avg=total/num \n",
    "\n",
    "limit=float(input(\"\\nWhat is your daily calorie limit?\\n\"))\n",
    "\n",
    "print(\"\\n\\n----- Your Calorie Report -----\")\n",
    "print(\"-\"*35)\n",
    "print(\"Meal Name\\t\\tCalories\")\n",
    "print(\"-\"*35)\n",
    "\n",
    "for i in range(num):\n",
    "    print(f\"{meal_l[i].ljust(20)}\\t {cal_l[i]}\")\n",
    "    print()\n",
    "print(\"-\"*35)\n",
    "\n",
    "print(f\"Total Calories:\\t\\t{total:.2f}\")\n",
    "\n",
    "print(f\"Average Calories/Meal:\\t{avg:.2f}\")\n",
    "\n",
    "print(f\"Your Daily Limit:\\t{limit:.2f}\")\n",
    "\n",
    "print(\"-\"*35)\n",
    "l_stat=\"\"\n",
    "\n",
    "sub=total-limit\n",
    "if total>limit:\n",
    "    print(f\"\\n⚠️  Warning! You are {sub:.2f} calories OVER your daily limit. ⚠️\")\n",
    "    l_stat = f\"Over limit by {sub:.2f} calories.\"\n",
    "\n",
    "else:\n",
    "    print(f\"\\n✅  Success! You are within your daily limit. ✅\\nYou have {-sub:.2f} calories left.\")\n",
    "    l_stat = f\"Under limit by {-sub:.2f} calories.\"\n",
    "    \n",
    "s=input(\"\\nWould you like to save this session to a log file? (yes/no): \").lower()\n",
    "if s in ['yes', 'y']:\n",
    "    with open(\"calorie.txt\", \"a\") as f: \n",
    "        f.write(\"--- Calorie Session Log ---\\n\")\n",
    "        f.write(f\"Timestamp: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\\n\")\n",
    "        f.write(\"-\"*30 + \"\\n\")\n",
    "\n",
    "        for i in range(num):\n",
    "            f.write(f\"{meal_l[i]} {cal_l[i]}\\n\")\n",
    "        f.write(\"-\"*30 + \"\\n\")\n",
    "        f.write(f\"Total Calories: {total:.2f}\\n\")\n",
    "        f.write(f\"Average Calories: {avg:.2f}\\n\")\n",
    "        f.write(f\"Daily Limit: {limit:.2f}\\n\")\n",
    "        f.write(f\"Status: {l_stat}\\n\")\n",
    "        f.write(\"-\"*30 + \"\\n\\n\")\n",
    "    print(\"Session saved successfully to calorie.txt\")\n",
    "else:\n",
    "    print(\"Log not saved. Have a great day!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "807ef342-b5e2-4122-a8ed-284817a9d633",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
