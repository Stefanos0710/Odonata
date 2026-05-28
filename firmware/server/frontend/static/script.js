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
  const videoStream  = $("#video-stream");
  const videoOverlay = $("#video-overlay");
  const servoSlider  = $("#servo-slider");
  const servoValue   = $("#servo-value");
  const batteryFill  = $("#battery-fill");
  const batteryPct   = $("#battery-pct");

  // ─── Video Stream ────────────────────────────────
  let videoStreamActive = false;
  let videoAnimFrame     = null;
  const ctx = videoCanvas.getContext("2d");
  let peerConnection = null;

  /**
   * Draw a static noise pattern on the canvas as a placeholder
   * when the real camera stream is unavailable.
   */
  function drawNoise() {
    videoStream.style.display = "none";
    videoCanvas.style.display = "block";
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

  async function startWebRTC() {
    peerConnection = new RTCPeerConnection();
    
    // Play the stream when it arrives
    peerConnection.addEventListener("track", (evt) => {
      stopVideoLoop(); // Stop noise
      videoCanvas.style.display = "none";
      videoStream.style.display = "block";
      if (videoStream.srcObject !== evt.streams[0]) {
        videoStream.srcObject = evt.streams[0];
      }
    });

    peerConnection.addTransceiver('video', { direction: 'recvonly' });

    const offer = await peerConnection.createOffer();
    await peerConnection.setLocalDescription(offer);

    try {
      const response = await fetch("/api/webrtc/offer", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          sdp: peerConnection.localDescription.sdp,
          type: peerConnection.localDescription.type
        })
      });
      const answer = await response.json();
      if (answer.sdp) {
        await peerConnection.setRemoteDescription(new RTCSessionDescription(answer));
      } else {
        console.error("WebRTC Error:", answer);
        startVideoLoop();
      }
    } catch (e) {
      console.error("Failed to start WebRTC:", e);
      startVideoLoop();
    }
  }

  function stopWebRTC() {
    if (peerConnection) {
      peerConnection.close();
      peerConnection = null;
    }
    videoStream.srcObject = null;
    videoStream.style.display = "none";
    videoCanvas.style.display = "block";
  }

  videoToggle.addEventListener("change", () => {
    videoStreamActive = videoToggle.checked;

    if (videoStreamActive) {
      videoOverlay.classList.add("hidden");
      startVideoLoop();
      startWebRTC();
    } else {
      videoOverlay.classList.remove("hidden");
      stopWebRTC();
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

  // API ENDPOINTS //
  async function sendCommand(url, payload = {}) {
    try {
      const response = await fetch(url, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });
      return await response.json();
    } catch (error) {
      console.error(`API-Fehler bei ${url}:`, error);
    }
  }

  // Is the drone connected?
  function setConnected(connected) {
    if (connected) {
      statusPill.classList.add("connected");
      statusPill.innerHTML = '<span class="status-dot"></span>Connected';
    } else {
      statusPill.classList.remove("connected");
      statusPill.innerHTML = '<span class="status-dot"></span>Disconnected';
    }
  }


  // the 3 main actions: start/stop drone, start flight
  $("#btn-start-drone").addEventListener("click", () => {
    console.log("Start Drone requested");
    sendCommand("/api/drone/start");
  });

  $("#btn-stop-drone").addEventListener("click", () => {
    console.log("Stop Drone requested");
    sendCommand("/api/drone/stop");
  });

  $("#btn-start-flight").addEventListener("click", () => {
    console.log("Start Flight requested");
    sendCommand("/api/flight/start");
  });

  // Connect Drone Modal logic
  const modal = $("#connect-modal");
  const btnConnectDrone = $("#btn-connect-drone");
  const btnCloseModal = $("#close-modal");
  const ipList = $("#connected-ips-list");
  const btnManualConnect = $("#btn-manual-connect");
  const manualIpInput = $("#manual-ip");

  async function loadConnectedIps() {
    ipList.innerHTML = "<li>Loading IPs...</li>";
    try {
      const response = await fetch("/api/connected-ips");
      const data = await response.json();
      ipList.innerHTML = "";
      if (data.ips.length === 0) {
        ipList.innerHTML = "<li>No connected IPs found.</li>";
      } else {
        data.ips.forEach(device => {
          const li = document.createElement("li");
          
          const infoSpan = document.createElement("span");
          infoSpan.innerHTML = `<strong>${device.ip}</strong><br><small style="color:var(--text-muted);font-size:0.8em">${device.description}</small>`;
          
          const selectBtn = document.createElement("button");
          selectBtn.className = "btn-sm btn-primary";
          selectBtn.textContent = "Select";
          selectBtn.onclick = () => setDroneIp(device.ip);
          
          li.appendChild(infoSpan);
          li.appendChild(selectBtn);
          ipList.appendChild(li);
        });
      }
    } catch (e) {
      console.error(e);
      ipList.innerHTML = "<li>Failed to load IPs.</li>";
    }
  }

  async function setDroneIp(ip) {
    console.log("Setting drone IP to", ip);
    const result = await sendCommand("/api/set-drone-ip", { ip: ip });
    if (result && result.status === "success") {
      alert("Drone IP set successfully.");
      modal.style.display = "none";
    } else {
      alert("Failed to set Drone IP.");
    }
  }

  btnConnectDrone.addEventListener("click", () => {
    modal.style.display = "flex";
    loadConnectedIps();
  });

  btnCloseModal.addEventListener("click", () => {
    modal.style.display = "none";
  });

  btnManualConnect.addEventListener("click", () => {
    const ip = manualIpInput.value.trim();
    if (ip) {
      setDroneIp(ip);
    }
  });

  // Close modal when clicking outside
  window.addEventListener("click", (e) => {
    if (e.target === modal) {
      modal.style.display = "none";
    }
  });

  // motor controls
  $$(".motor-toggle").forEach((btn) => {
    btn.addEventListener("click", () => {
      const motorNum = parseInt(btn.dataset.motor);
      const throttleVal = parseFloat($(`#motor${motorNum}-throttle`).value);
      
      console.log(`Motor ${motorNum}: START at throttle ${throttleVal}`);
      // Sendet die Daten passend zum Pydantic-Modell des Servers
      sendCommand("/api/motor/test", {
        motor_number: motorNum,
        throttle: throttleVal,
        duration: 2.0
      });
    });
  });

  $$(".motor-stop").forEach((btn) => {
    btn.addEventListener("click", () => {
      const motorNum = parseInt(btn.dataset.motor);
      console.log(`Motor ${motorNum}: STOP`);
      
      // Setzt den Motor sofort für eine minimale Dauer auf 0.0 Throttle
      sendCommand("/api/motor/test", {
        motor_number: motorNum,
        throttle: 0.0,
        duration: 0.1
      });
    });
  });

  // battery status update
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

  // update the battery status 
  updateBattery(0);

  // servo slider 
  servoSlider.addEventListener("input", () => {
    const currentAngle = parseInt(servoSlider.value);
    servoValue.textContent = currentAngle;
    
    // send the current angle to the server
    sendCommand("/api/servo/move", { angle: currentAngle });
  });


  // Simulate connection after 1 second (remove when real API is wired)
  // setTimeout(() => setConnected(true), 1000);

  // Expose helpers globally for debugging / future integration
  window.odonata = {
    updateBattery,
    setConnected,
  };
})();
