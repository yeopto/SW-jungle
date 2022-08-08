const res = {
    "wait" : [
        {   
            "interview_date": "2022-07-12", // 면접일자
            "worker_name": '김땅콩',     // 알바생 이름
            "interview_time": 14,         // 면접시간(24시기준)
            "question": "산책 좋아하세요?",             // 거절여부(사장님이 거절), 1이 거절 0이 수락
        },
        
    ]
    "will" : [
        {
            "interview_date": "2022-07-12", // 면접일자
            "worker_name": '김땅콩',     // 알바생 이름
            "interview_time": 14,         // 면접시간(24시기준)
            "question": "산책 좋아하세요?",             // 거절여부(사장님이 거절), 1이 거절 0이 수락
        },
    ]
    "complete" : [

    ]

}

console.log(res["result"][0].interview_date.split('-'));