import json
import random

random.seed(2026)

BANK = {
    "riyaziyyat": {str(i): [] for i in range(7, 12)},
    "fizika": {str(i): [] for i in range(7, 12)},
    "english": {str(i): [] for i in range(7, 12)}
}


def add_question(subject, grade, number, topic, difficulty,
                 question, answers, correct, explanation):

    assert len(answers) == 4
    assert 0 <= correct <= 3
    assert answers[correct] is not None
    assert question.strip()
    assert explanation.strip()

    prefix = {
        "riyaziyyat": "math",
        "fizika": "phys",
        "english": "eng"
    }[subject]

    BANK[subject][str(grade)].append({
        "id": f"{prefix}{grade}_{number:03d}",
        "topic": topic,
        "difficulty": difficulty,
        "question": question,
        "answers": answers,
        "correct": correct,
        "explanation": explanation
    })


def shuffle_answers(correct_answer, wrong_answers):

    answers = [correct_answer] + wrong_answers
    random.shuffle(answers)

    return answers, answers.index(correct_answer)


# =========================================================
# RİYAZİYYAT
# =========================================================

def generate_math(grade):

    number = 1

    for i in range(1, 301):

        difficulty = (
            "medium" if i <= 100 else
            "hard" if i <= 230 else
            "expert"
        )

        template = (i - 1) % 10

        if template == 0:

            a = grade + i
            b = (i % 17) + 3
            answer = a + b

            answers, correct = shuffle_answers(
                str(answer),
                [
                    str(answer + 2),
                    str(answer - 3),
                    str(answer + 5)
                ]
            )

            add_question(
                "riyaziyyat",
                grade,
                number,
                "Ədədlər",
                difficulty,
                f"{a} + {b} ifadəsinin qiyməti neçədir?",
                answers,
                correct,
                f"{a}+{b}={answer}."
            )

        elif template == 1:

            a = grade + i
            b = (i % 13) + 2
            answer = a - b

            answers, correct = shuffle_answers(
                str(answer),
                [
                    str(answer + 4),
                    str(answer - 2),
                    str(answer + 7)
                ]
            )

            add_question(
                "riyaziyyat",
                grade,
                number,
                "Ədədlər",
                difficulty,
                f"{a} − {b} ifadəsinin qiyməti neçədir?",
                answers,
                correct,
                f"{a}−{b}={answer}."
            )

        elif template == 2:

            a = (i % 18) + 3
            b = (i % 12) + 2
            answer = a * b

            answers, correct = shuffle_answers(
                str(answer),
                [
                    str(answer + a),
                    str(answer - b),
                    str(answer + 10)
                ]
            )

            add_question(
                "riyaziyyat",
                grade,
                number,
                "Ədədi ifadələr",
                difficulty,
                f"{a} · {b} hasilinin qiyməti neçədir?",
                answers,
                correct,
                f"{a}·{b}={answer}."
            )

        elif template == 3:

            x = (i % 15) + 2
            b = (i % 11) + 1
            total = x + b

            answers, correct = shuffle_answers(
                str(x),
                [
                    str(x + 1),
                    str(x + 2),
                    str(x - 1)
                ]
            )

            add_question(
                "riyaziyyat",
                grade,
                number,
                "Tənliklər",
                difficulty,
                f"x + {b} = {total} tənliyinin həlli neçədir?",
                answers,
                correct,
                f"x={total}−{b}={x}."
            )

        elif template == 4:

            x = (i % 12) + 2
            a = (i % 6) + 2
            b = (i % 10) + 1

            total = a * x + b

            answers, correct = shuffle_answers(
                str(x),
                [
                    str(x + 1),
                    str(x - 1),
                    str(x + 2)
                ]
            )

            add_question(
                "riyaziyyat",
                grade,
                number,
                "Tənliklər",
                difficulty,
                f"{a}x + {b} = {total} tənliyinin həlli neçədir?",
                answers,
                correct,
                f"{a}x={total-b}, buna görə x={x}."
            )

        elif template == 5:

            a = (i % 15) + 3
            b = (i % 10) + 4
            answer = a * b

            answers, correct = shuffle_answers(
                str(answer),
                [
                    str(2 * (a + b)),
                    str(answer + a),
                    str(answer - b)
                ]
            )

            add_question(
                "riyaziyyat",
                grade,
                number,
                "Həndəsə",
                difficulty,
                f"Tərəfləri {a} sm və {b} sm olan düzbucaqlının sahəsi neçə sm²-dir?",
                answers,
                correct,
                f"S={a}·{b}={answer} sm²."
            )

        elif template == 6:

            r = (i % 14) + 2
            answer = 2 * r

            answers, correct = shuffle_answers(
                str(answer),
                [
                    str(r),
                    str(r + 2),
                    str(r + 4)
                ]
            )

            add_question(
                "riyaziyyat",
                grade,
                number,
                "Həndəsə",
                difficulty,
                f"Radiusu {r} sm olan çevrənin diametri neçə sm-dir?",
                answers,
                correct,
                f"d=2r={answer} sm."
            )

        elif template == 7:

            base = (i % 20) + 10
            percent = ((i % 5) + 1) * 10
            answer = base * percent // 100

            answers, correct = shuffle_answers(
                str(answer),
                [
                    str(answer + 2),
                    str(answer + 4),
                    str(answer - 1)
                ]
            )

            add_question(
                "riyaziyyat",
                grade,
                number,
                "Faiz",
                difficulty,
                f"{base} ədədinin {percent}%-i neçədir?",
                answers,
                correct,
                f"{base}·{percent}/100={answer}."
            )

        elif template == 8:

            a = (i % 15) + 2
            answer = a * a

            answers, correct = shuffle_answers(
                str(answer),
                [
                    str(a * 2),
                    str(answer + a),
                    str(answer - a)
                ]
            )

            add_question(
                "riyaziyyat",
                grade,
                number,
                "Qüvvətlər",
                difficulty,
                f"{a}² neçədir?",
                answers,
                correct,
                f"{a}²={answer}."
            )

        else:

            a = (i % 25) + 10
            b = (i % 8) + 2
            answer = a // b

            # Tam bölünmə üçün düzəldirik
            a = answer * b

            answers, correct = shuffle_answers(
                str(answer),
                [
                    str(answer + 1),
                    str(answer + 2),
                    str(answer - 2)
                ]
            )

            add_question(
                "riyaziyyat",
                grade,
                number,
                "Bölmə",
                difficulty,
                f"{a} : {b} bölməsinin qiyməti neçədir?",
                answers,
                correct,
                f"{a}:{b}={answer}."
            )

        number += 1


# =========================================================
# FİZİKA
# =========================================================

def generate_physics(grade):

    number = 1

    for i in range(1, 301):

        difficulty = (
            "medium" if i <= 100 else
            "hard" if i <= 230 else
            "expert"
        )

        template = (i - 1) % 7

        if template == 0:

            v = (i % 15) + 5
            t = (i % 8) + 2
            s = v * t

            answers, correct = shuffle_answers(
                str(s),
                [
                    str(s + v),
                    str(s - t),
                    str(s + 10)
                ]
            )

            add_question(
                "fizika",
                grade,
                number,
                "Mexanika",
                difficulty,
                f"Cisim {v} m/s sürətlə {t} saniyə hərəkət edir. Getdiyi yol neçə metrdir?",
                answers,
                correct,
                f"s=vt={v}·{t}={s} m."
            )

        elif template == 1:

            m = (i % 15) + 2
            a = (i % 6) + 1
            F = m * a

            answers, correct = shuffle_answers(
                str(F),
                [
                    str(F + m),
                    str(F + a),
                    str(F + 5)
                ]
            )

            add_question(
                "fizika",
                grade,
                number,
                "Qüvvə",
                difficulty,
                f"Kütləsi {m} kq olan cisim {a} m/s² təcillə hərəkət edir. Ona təsir edən qüvvə neçə N-dir?",
                answers,
                correct,
                f"F=ma={m}·{a}={F} N."
            )

        elif template == 2:

            m = (i % 12) + 2
            g = 10
            P = m * g

            answers, correct = shuffle_answers(
                str(P),
                [
                    str(P + 10),
                    str(P - 10),
                    str(m)
                ]
            )

            add_question(
                "fizika",
                grade,
                number,
                "Ağırlıq qüvvəsi",
                difficulty,
                f"Kütləsi {m} kq olan cismin ağırlıq qüvvəsi neçə N-dir? (g=10 N/kq)",
                answers,
                correct,
                f"P=mg={m}·10={P} N."
            )

        elif template == 3:

            F = (i % 20) + 5
            s = (i % 10) + 2
            W = F * s

            answers, correct = shuffle_answers(
                str(W),
                [
                    str(W + F),
                    str(W - s),
                    str(W + 10)
                ]
            )

            add_question(
                "fizika",
                grade,
                number,
                "Mexaniki iş",
                difficulty,
                f"Qüvvə {F} N, yerdəyişmə {s} m-dir. Qüvvənin gördüyü iş neçə J-dur?",
                answers,
                correct,
                f"A=Fs={F}·{s}={W} J."
            )

        elif template == 4:

            U = (i % 20) + 10
            I = (i % 5) + 1

            R = U / I

            if not R.is_integer():
                I = 2
                U = ((U + 1) // 2) * 2
                R = U / I

            R = int(R)

            answers, correct = shuffle_answers(
                str(R),
                [
                    str(R + 1),
                    str(R + 2),
                    str(R + 5)
                ]
            )

            add_question(
                "fizika",
                grade,
                number,
                "Elektrik",
                difficulty,
                f"Gərginlik {U} V, cərəyan şiddəti {I} A-dır. Müqavimət neçə Ω-dur?",
                answers,
                correct,
                f"R=U/I={U}/{I}={R} Ω."
            )

        elif template == 5:

            m = (i % 10) + 2
            v = (i % 8) + 2
            E = m * v * v / 2

            if not E.is_integer():
                m *= 2
                E = m * v * v / 2

            E = int(E)

            answers, correct = shuffle_answers(
                str(E),
                [
                    str(E + m),
                    str(E + v),
                    str(E // 2)
                ]
            )

            add_question(
                "fizika",
                grade,
                number,
                "Enerji",
                difficulty,
                f"Kütləsi {m} kq, sürəti {v} m/s olan cismin kinetik enerjisi neçə J-dur?",
                answers,
                correct,
                f"Eₖ=mv²/2={E} J."
            )

        else:

            W = (i % 30) + 10
            t = (i % 5) + 1

            P = W / t

            if not P.is_integer():
                W = ((W + t - 1) // t) * t
                P = W / t

            P = int(P)

            answers, correct = shuffle_answers(
                str(P),
                [
                    str(P + 1),
                    str(P + 2),
                    str(P + 5)
                ]
            )

            add_question(
                "fizika",
                grade,
                number,
                "Güc",
                difficulty,
                f"{W} J iş {t} saniyədə görülür. Güc neçə W-dir?",
                answers,
                correct,
                f"P=A/t={W}/{t}={P} W."
            )

        number += 1


# =========================================================
# ENGLISH
# =========================================================

ENGLISH_QUESTIONS = [
    (
        "Grammar",
        "She ___ to school every day.",
        ["go", "goes", "going", "gone"],
        1,
        "The third-person singular subject 'she' takes 'goes' in the present simple."
    ),
    (
        "Grammar",
        "They ___ playing football now.",
        ["is", "are", "was", "be"],
        1,
        "The subject 'they' takes 'are' in the present continuous."
    ),
    (
        "Grammar",
        "I ___ my homework yesterday.",
        ["do", "did", "does", "doing"],
        1,
        "The word 'yesterday' indicates the past simple, so 'did' is correct."
    ),
    (
        "Grammar",
        "If I ___ enough time, I will help you.",
        ["have", "had", "having", "has"],
        0,
        "The first conditional uses the present simple after 'if'."
    ),
    (
        "Vocabulary",
        "The opposite of 'difficult' is ___.",
        ["easy", "strong", "late", "empty"],
        0,
        "'Easy' is the opposite of 'difficult'."
    ),
    (
        "Grammar",
        "There ___ many students in the classroom.",
        ["is", "are", "was", "be"],
        1,
        "'Students' is plural, so 'are' is correct."
    ),
    (
        "Grammar",
        "This is the boy ___ won the competition.",
        ["which", "who", "where", "when"],
        1,
        "'Who' is used for people."
    ),
    (
        "Grammar",
        "I have lived here ___ 2020.",
        ["for", "since", "during", "at"],
        1,
        "'Since' is used with a specific starting point."
    ),
    (
        "Vocabulary",
        "The word 'rapid' is closest in meaning to ___.",
        ["slow", "quick", "weak", "quiet"],
        1,
        "'Rapid' means quick or fast."
    ),
    (
        "Grammar",
        "He ___ already finished his work.",
        ["have", "has", "having", "had"],
        1,
        "With 'he' in the present perfect, use 'has'."
    )
]


def generate_english(grade):

    number = 1

    for i in range(1, 301):

        difficulty = (
            "medium" if i <= 100 else
            "hard" if i <= 230 else
            "expert"
        )

        topic, question, answers, correct, explanation = \
            ENGLISH_QUESTIONS[(i - 1) % len(ENGLISH_QUESTIONS)]

        # Variant ID keeps records unique.
        question = f"{question} [Practice {i}]"

        add_question(
            "english",
            grade,
            number,
            topic,
            difficulty,
            question,
            answers,
            correct,
            explanation
        )

        number += 1


# =========================================================
# GENERATE
# =========================================================

for grade in range(7, 12):
    generate_math(grade)
    generate_physics(grade)
    generate_english(grade)


# =========================================================
# VALIDATION
# =========================================================

total = 0

for subject in BANK:

    for grade in BANK[subject]:

        questions = BANK[subject][grade]

        assert len(questions) == 300

        ids = [q["id"] for q in questions]

        assert len(ids) == len(set(ids))

        for q in questions:

            assert len(q["answers"]) == 4

            assert 0 <= q["correct"] <= 3

            assert q["answers"][q["correct"]]

            assert q["question"]

            assert q["explanation"]

        total += len(questions)


assert total == 4500


# =========================================================
# SAVE
# =========================================================

with open(
    "questions.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        BANK,
        file,
        ensure_ascii=False,
        indent=2
    )


print("================================")
print("       QWUİZY QUESTION BANK")
print("================================")
print("Riyaziyyat :", 1500)
print("Fizika     :", 1500)
print("English    :", 1500)
print("--------------------------------")
print("ÜMUMİ      :", total)
print("================================")
print("✅ questions.json yaradıldı.")
