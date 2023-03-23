#!/usr/bin/env python3

import random

def display_quotes():
    quotes = ["We tend to think of great thinkers and innovators as soloists, but the truth is that the greatest innovative thinking doesn't occur in a vacuum. Innovation results from collaboration. John C. Maxwell", "Some of us think holding on makes us strong, but sometimes it is letting go. Hermann Hesse", "But what I've discovered over time is that some of the wisest people I know have also been some of the most broken people. James Prescott, Mosaic of Grace", "Don't waste your time with explanations, people only hear what they want to hear. Paulo Coelho", "To make difficult decisions wisely, it helps to have a systematic process for assessing each choice and its consequences - the potential impact on each aspect of your life. Stedman Graham, You Can Make It Happen Every Day", "Each of us experiences defeats in life. We can transform defeat into victory if we learn from life’s whuppings. Les Brown", "To be wise, we must seek Jesus, for we will not find wisdom apart from him. Kim Brenneman, Home Management", "Pain can change you, but that doesn't mean it has to be a bad change. Take that pain and turn it into wisdom. Dalai Lama", "Meditation is about viewing the world with great clarity so you can make wise decisions. It will help you make the appropriate action with regard to things that you have to change. Mia Conrad, Social Anxiety"]
    generator = random.randrange(0, len(quotes))
    print(quotes[generator], end = "")
    

print(display_quotes())
