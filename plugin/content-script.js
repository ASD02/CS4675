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

let posts = document.getElementsByClassName("Post")

for (let post_element of posts) {
    post_react = post_element.getElementsByClassName("postReact").item(0)

    let upvoteButton = document.createElement("button");
    upvoteButton.className = "vote-button";
    let upvoteImage = document.createElement("img");
    upvoteImage.src = chrome.runtime.getURL("images/check-mark.png");;
    upvoteButton.appendChild(upvoteImage);
    post_react.appendChild(upvoteButton);

    let downvoteButton = document.createElement("button");
    downvoteButton.className = "vote-button";
    let downvoteImage = document.createElement("img");
    downvoteImage.src = chrome.runtime.getURL("images/flag.png");;
    downvoteButton.appendChild(downvoteImage);
    post_react.appendChild(downvoteButton);

    let gaugeTarget = document.createElement("canvas");
    post_react.appendChild(gaugeTarget);

    let gauge = new Gauge(gaugeTarget).setOptions(opts);
    gauge.maxValue = 100;
    gauge.setMinValue(0);
    gauge.animationSpeed = 32;
    gauge.set(+Math.random()*100);
}
