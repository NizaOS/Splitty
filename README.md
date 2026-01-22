<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
</head>
<body style="font-family: Arial, sans-serif; max-width: 900px; margin: 0 auto; padding: 20px; line-height: 1.6;">

  <header style="text-align: center; margin-bottom: 40px;">
        <h1 style="font-size: 3em; margin-bottom: 10px;">SPLITTY</h1>
        <p style="font-size: 1.2em; color: #555;">A 40% Wireless Split Mechanical Keyboard</p>
        <p><b>Low Profile &bull; Choc v1 &bull; ZMK Firmware &bull; 1000mAh Battery Life</b></p>
        <hr>
    </header>
    <section>
        <h2>Project Overview</h2>
        <p>SPLITTY is a custom-built, wireless split keyboard designed for portability and ergonomics. It utilizes the <b>Seeed Studio XIAO nRF52840</b> for Bluetooth 5.0 connectivity and is built on a custom PCB optimized for <b>Kailh Choc v1</b> low-profile switches.</p>
        <h3>Technical Specifications</h3>
        <ul>
            <li><b>Microcontroller:</b> 2x Seeed Studio XIAO nRF52840 (Bluetooth 5.0)</li>
            <li><b>Switch Type:</b> Kailh Choc v1 (PG1350) - Linear/Tactile/Clicky</li>
            <li><b>Battery:</b> 2x 1000mAh LiPo (WLY394058) - Approx. 1+ month battery life</li>
            <li><b>PCB Features:</b> Hotswap support, reversible footprint, 1.2mm thickness</li>
            <li><b>Firmware:</b> ZMK (Wireless-first firmware)</li>
        </ul>
    </section>
    <hr>
    <section>
        <h2>Bill of Materials (BOM)</h2>
        <p><i>Prices estimated in USD based on INR conversion ($1 &#8776; &#8377;90.27).</i></p>
                <table border="1" cellpadding="10" cellspacing="0" style="width: 100%; border-collapse: collapse; text-align: left;">
            <thead>
                <tr style="background-color: #f2f2f2;">
                    <th>Component</th>
                    <th>Qty</th>
                    <th>Unit Price</th>
                    <th>Total (USD)</th>
                    <th>Sourcing Link</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><b>Seeed XIAO BLE nRF52840</b></td>
                    <td>2</td>
                    <td>$14.88</td>
                    <td>$25.87</td>
                    <td><a href="https://www.fabtolab.com/seeed-xiao-ble-nrf52840-supports-arduino-micropython-bluetooth5.0-onboard-antenna-microcontroller-32-bit-arm-cortex-m4" target="_blank">Fab.to.Lab</a></td>
                </tr>
                <tr>
                    <td><b>Kailh Choc v1 Switches</b></td>
                    <td>40</td>
                    <td>$0.55</td>
                    <td>$22.00</td>
                    <td><a href="https://neomacro.in/products/kailh-choc-pg1350-hot-swap-sockets?srsltid=AfmBOor8u36EImYNmOMVrunXb-IJBcmzE4elqdvKx1VKok2jcNJwbEJO" target="_blank">NeoMacro</a></td>
                </tr>
                <tr>
                    <td><b>Choc Hotswap Sockets</b></td>
                    <td>40</td>
                    <td>$0.18</td>
                    <td>$7.00</td>
                    <td><a href="https://neomacro.in/products/kailh-choc-v1-switches" target="_blank">NeoMacro</a></td>
                </tr>
                <tr>
                    <td><b>MBK/MCC Keycaps</b></td>
                    <td>40</td>
                    <td>$0.40</td>
                    <td>$16.00</td>
                    <td><a href="https://neomacro.in/products/chocfox-cfx-choc-blank-keycaps?variant=49467027685654" target="_blank">NeoMacro</a></td>
                </tr>
                <tr>
                    <td><b>PCB (Manufacturing)</b></td>
                    <td>1</td>
                    <td>$21.00</td>
                    <td>$21.00</td>
                    <td><a href="https://jlcpcb.com/" target="_blank">JLCPCB</a></td>
                </tr>
                <tr>
                    <td><b>3D Printed Case (Shipping)</b></td>
                    <td>1</td>
                    <td>$10.00</td>
                    <td>$10.00</td>
                    <td>Printing Legion</td>
                </tr>
                <tr>
                    <td><b>LiPo Battery (1000mAh)</b><br><small>Model: WLY394058 (3.9mm thick)</small></td>
                    <td>2</td>
                    <td>$4.18</td>
                    <td>$8.36</td>
                    <td><a href="https://robu.in/product/wly394058-1000mah-3-7v-single-cell-rechargeable-lipo-battery/" target="_blank">Robu.in</a></td>
                </tr>
                <tr>
                    <td><b>1N4148W Diodes (SOD-123)</b></td>
                    <td>40</td>
                    <td>$0.006</td>
                    <td>$0.24</td>
                    <td><a href="https://robu.in/product/1n4148w-sod-123-1206-diodereel-of-3000/" target="_blank">Robu.in</a></td>
                </tr>
                <tr>
                    <td><b>806K1 Resistor (0805)</b></td>
                    <td>10</td>
                    <td>$0.023</td>
                    <td>$$0.14</td>
                    <td><a href="https://robu.in/product/ac0402fr-07806kl-yageo-62-5mw-thick-film-resistors-50v-±100ppm-℃-±1-806kω-0402-chip-resistor-surface-mount-rohs/" target="_blank">Robu.in</a></td>
                </tr>
                <tr>
                    <td><b>2M1 Resistor (0805)</b></td>
                    <td>10</td>
                    <td>$0.020</td>
                    <td>$$0.11</td>
                    <td><a href="https://robu.in/product/rc0603fr-0716rl-yageo-smd-chip-resistor-16-ohm-±-1-100-mw-0603-1608-metric-thick-film-general-purpose/" target="_blank">Robu.in</a></td>
                </tr>
                <tr style="font-weight: bold; background-color: #e6e6e6;">
                    <td colspan="3" style="text-align: right;">ESTIMATED TOTAL</td>
                    <td colspan="2">$110.72</td>
                </tr>
            </tbody>
        </table>
    </section>

   <hr>

 

   <div id="gallery" style="padding: 20px; background-color: #f9f9f9; border: 1px solid #ddd; margin-top: 30px;">
        <h2 style="text-align: center;">Project Gallery</h2>
      <img width="2628" height="1708" alt="Screenshot 2026-01-07 at 18 36 32" src="https://github.com/user-attachments/assets/810bef78-5737-4d3a-881b-fcd5a2a62d03" />
<img width="2626" height="1709" alt="Screenshot 2026-01-07 at 18 37 47" src="https://github.com/user-attachments/assets/fa6ffa10-7468-4aaf-90e2-445f281ef5a1" />


</div>
</div>

</body>
</html>
