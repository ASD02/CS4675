var opts = {
    angle: -0.2,
    lineWidth: 0.4,
    radiusScale: 1,
    pointer: {
        length: 0.6,
        strokeWidth: 0.035,
        color: '#000000'
    },
    limitMax: true,
    limitMin: true,
    generateGradient: true,
    percentColors: [[0.0, "#FF0000"], [0.5, "#FFEE00"], [1.0, "#00B300"]],
    highDpiSupport: true
};

const user_id = 525;

let posts = document.getElementsByClassName("Post")

for (let post_element of posts) {
    let post_id = post_element.id

    // TODO: Call GET API to get score
    const request = new Request(`http://localhost:5000/score/${post_id}`, {
        method: "GET"
    });
    fetch(request)
        .then(
            (response) => {
                let post_react = post_element.getElementsByClassName("postReact").item(0)

                let upvoteButton = document.createElement("button");
                upvoteButton.className = "vote-button";
                let upvoteImage = document.createElement("img");
                upvoteImage.src = chrome.runtime.getURL("images/check-mark.png");
                upvoteButton.appendChild(upvoteImage);
                post_react.appendChild(upvoteButton);
                // TODO: Add onClick listeners

                let downvoteButton = document.createElement("button");
                downvoteButton.className = "vote-button";
                let downvoteImage = document.createElement("img");
                downvoteImage.src = chrome.runtime.getURL("images/flag.png");
                downvoteButton.appendChild(downvoteImage);
                post_react.appendChild(downvoteButton);
                // TODO: Add onClick listeners

                let gaugeTarget = document.createElement("canvas");
                post_react.appendChild(gaugeTarget);

                response.json().then((json_) => {
                    let trustScore = json_['score'];
                    if (trustScore == -1) {
                        post_react.removeChild(gaugeTarget);
                        let opinionImage = document.createElement("img");
                        opinionImage.src = chrome.runtime.getURL("images/opinion.png");
                        opinionImage.className = "opinion-image"
                        opinionImage.title = "The model detected that this post is an opinion!"
                        post_react.appendChild(opinionImage);
                    } else {
                        let gauge = new Gauge(gaugeTarget).setOptions(opts);
                        gauge.maxValue = 100;
                        gauge.setMinValue(0);
                        gauge.animationSpeed = 32;
                        gauge.set(json_['score']);

                        gaugeTarget.title = `
                        Trust Score: ${json_['score']}\n
Upvotes: ${json_['positive_votes']}\n
Downvotes: ${json_['negative_votes']}\n
Model Prediction: ${json_['model_prediction'] == -1 ? 'Fake News' : 'True News'}\n
                        `
                        // TODO: Add tooltip (title) to display stats
                    }
                })
            },
            (error) => {
                console.error(error);
            });
}
