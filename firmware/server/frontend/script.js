/* ===================================================
   Odonata Cockpit — Frontend Logic
   =================================================== */

(function () {
  "use strict";

  // ─── DOM references ──────────────────────────────
  const $ = (sel) => document.querySelector(sel);
  const $$ = (sel) => document.querySelectorAll(sel);

  const videoToggle  = $("#video-toggle");
  const videoCanvas  = $("#video-canvas");
  const videoOverlay = $("#video-overlay");
  const servoSlider  = $("#servo-slider");
  const servoValue   = $("#servo-value");
  const batteryFill  = $("#battery-fill");
  const batteryPct   = $("#battery-pct");

  // ─── Video Stream ────────────────────────────────
  let videoStreamActive = false;
  let videoAnimFrame     = null;
  const ctx = videoCanvas.getContext("2d");

  /**
   * Draw a static noise pattern on the canvas as a placeholder
   * when the real camera stream is unavailable.
   */
  function drawNoise() {
    const w = videoCanvas.width;
    const h = videoCanvas.height;
    const imageData = ctx.createImageData(w, h);
    const data = imageData.data;

    for (let i = 0; i < data.length; i += 4) {
      const v = Math.random() * 40 + 15; // dark noise
      data[i]     = v;
      data[i + 1] = v;
      data[i + 2] = v;
      data[i + 3] = 255;
    }
    ctx.putImageData(imageData, 0, 0);

    // overlay a subtle "No Signal" label
    ctx.fillStyle = "rgba(212, 215, 224, .25)";
    ctx.font = "600 14px Inter, sans-serif";
    ctx.textAlign = "center";
    ctx.fillText("NO SIGNAL", w / 2, h / 2);
  }

  function startVideoLoop() {
    function loop() {
      drawNoise();
      videoAnimFrame = requestAnimationFrame(loop);
    }
    loop();
  }

  function stopVideoLoop() {
    if (videoAnimFrame) {
      cancelAnimationFrame(videoAnimFrame);
      videoAnimFrame = null;
    }
    ctx.clearRect(0, 0, videoCanvas.width, videoCanvas.height);
  }

  videoToggle.addEventListener("change", () => {
    videoStreamActive = videoToggle.checked;

    if (videoStreamActive) {
      videoOverlay.classList.add("hidden");
      startVideoLoop();
      // TODO: connect to actual MJPEG / WebSocket stream from drone
      // Example: const img = new Image();
      //          img.onload = () => ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
      //          img.src = "/stream?t=" + Date.now();
    } else {
      videoOverlay.classList.remove("hidden");
      stopVideoLoop();
    }
  });

  // ─── Servo Slider ────────────────────────────────
  servoSlider.addEventListener("input", () => {
    servoValue.textContent = servoSlider.value;
  });

  // ─── Battery ─────────────────────────────────────
  /**
   * Update the battery UI.
   * @param {number} pct  Battery percentage (0-100)
   */
  function updateBattery(pct) {
    pct = Math.max(0, Math.min(100, pct));
    batteryPct.textContent = pct;
    batteryFill.style.width = pct + "%";

    batteryFill.classList.remove("low", "mid");
    if (pct <= 20) {
      batteryFill.classList.add("low");
    } else if (pct <= 50) {
      batteryFill.classList.add("mid");
    }
  }

  // Initialise battery display with placeholder value
  updateBattery(99);

  // ─── Motor buttons ──────────────────────────────
  $$(".motor-toggle").forEach((btn) => {
    btn.addEventListener("click", () => {
      const motor = btn.dataset.motor;
      const throttle = $(`#motor${motor}-throttle`).value;
      console.log(`Motor ${motor}: START at throttle ${throttle}`);
      // TODO: send command to server
    });
  });

  $$(".motor-stop").forEach((btn) => {
    btn.addEventListener("click", () => {
      const motor = btn.dataset.motor;
      console.log(`Motor ${motor}: STOP`);
      // TODO: send stop command to server
    });
  });

  // ─── Top-level action buttons ────────────────────
  $("#btn-start-drone").addEventListener("click", () => {
    console.log("Start Drone requested");
    // TODO: POST /api/drone/start
  });

  $("#btn-stop-drone").addEventListener("click", () => {
    console.log("Stop Drone requested");
    // TODO: POST /api/drone/stop
  });

  $("#btn-start-flight").addEventListener("click", () => {
    console.log("Start Flight requested");
    // TODO: POST /api/flight/start
  });

  // ─── Connection status (placeholder) ─────────────
  const statusPill = $("#status-pill");

  function setConnected(connected) {
    if (connected) {
      statusPill.classList.add("connected");
      statusPill.innerHTML = '<span class="status-dot"></span>Connected';
    } else {
      statusPill.classList.remove("connected");
      statusPill.innerHTML = '<span class="status-dot"></span>Disconnected';
    }
  }

  // Simulate connection after 1 second (remove when real API is wired)
  // setTimeout(() => setConnected(true), 1000);

  // Expose helpers globally for debugging / future integration
  window.odonata = {
    updateBattery,
    setConnected,
  };
})();
