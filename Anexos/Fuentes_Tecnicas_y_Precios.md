# Fuentes técnicas y precios

**Corte documental: 24-10-2026.** Las fichas de fabricante justifican funciones/puertos; una página de venta respalda un precio referencial y no una cotización de todas las unidades. Las reservas sin tarifa publicada permanecen identificadas. Las URL permiten revisar el documento completo.

## 1. Documentación primaria

- **S01. Cisco ISR1000 - ficha y licencias**: https://www.cisco.com/c/en/us/products/collateral/routers/1000-series-integrated-services-routers-isr/datasheet-c78-739512.html
- **S02. Cisco ISR1100/ISR1100X - retiro y productos de migración**: https://www.cisco.com/c/en/us/products/collateral/routers/1000-series-integrated-services-routers-isr/isr1100-isr1100x-series-routers-eol.html
- **S03. Cisco Catalyst9200 - avisos por hardware/software/licencia**: https://www.cisco.com/c/en/us/products/switches/catalyst-9200-series-switches/eos-eol-notice-listing.html
- **S04. Palo Alto - ciclo de vida de hardware**: https://www.paloaltonetworks.com/services/support/end-of-life-announcements/hardware-end-of-life-dates
- **S05. Cisco ISR2900 - funciones de la familia heredada**: https://www.cisco.com/c/en/us/products/collateral/routers/2900-series-integrated-services-routers-isr/data_sheet_c78_553896.html
- **S06. Cisco IP SLA y tracking - conmutación entre ISP**: https://www.cisco.com/c/en/us/support/docs/ip/ip-routing/200785-ISP-Failover-with-default-routes-using-I.html
- **S07. MikroTik Netwatch - sondas de alcance y calidad**: https://help.mikrotik.com/docs/spaces/ROS/pages/8323208/Netwatch
- **S08. MikroTik CCR2004**: https://mikrotik.com/product/ccr2004_16g_2splus
- **S09. MikroTik hEX E50UG**: https://mikrotik.com/product/hex_2024
- **S10. MikroTik CRS310**: https://mikrotik.com/product/crs310_8g_2s_in
- **S11. MikroTik DACXS+DA0001**: https://mikrotik.com/product/xs_da0001
- **S12. Deciso/OPNsense DEC3852**: https://shop.opnsense.com/product/dec3852-opnsense-rack-security-appliance/
- **S13. Proxmox - réplica de almacenamiento**: https://pve.proxmox.com/pve-docs/chapter-pvesr.html
- **S14. Proxmox - clúster y QDevice**: https://pve.proxmox.com/wiki/Cluster_Manager
- **S15. PCI SSC - objetivos y controles PCI DSS**: https://www.pcisecuritystandards.org/merchants/process/
- **S16. PCI SSC - biblioteca PCI DSS v4.0.1**: https://www.pcisecuritystandards.org/es/document_library/


## Partidas y fuentes de la alternativa A

| ID | Partida | Cantidad | Precio de origen | Evidencia | Fuente |
|---|---|---|---|---|---|
| router | Router sucursal, hardware base | 37 | 1032570 CLP_NET | PRECIO_PUBLICADO | https://www.ipexpress.cl/pyme/product_info.php/router-cisco-c1121x-8p-p-5439 |
| router_sec | Licencia SEC por router nuevo | 37 | 882.75 USD_NET | PRECIO_PUBLICADO | https://www.cdw.com/product/cisco-security-smart-license/5763463 |
| router_vperf | Licencia VPERF por router nuevo | 37 | 2200 USD_NET | RESERVA_INGENIERIA | https://www.cisco.com/c/en/us/products/collateral/routers/1000-series-integrated-services-routers-isr/datasheet-c78-739512.html |
| switch | Switch nuevo 24 puertos PoE, Network Essentials | 27 | 2109344 CLP_NET | PRECIO_PUBLICADO | https://www.ipexpress.cl/pyme/product_info.php/switch-cisco-c9200l-24p-4g-p-4179 |
| switch_term | Suscripción inicial switch nuevo, 3 años | 27 | 808.99 USD_NET | PRECIO_PUBLICADO_CONDICIONADO | https://www.cdw.com/product/cisco-digital-network-architecture-essentials-term-license-3-years-24/5380357 |
| stack_kit | Kit stack completo por miembro | 46 | 815 USD_NET | PRECIO_PUBLICADO | https://networkdevicesinc.com/products/c9200l-stack-kit |
| firewall | Firewall central hardware | 2 | 11385 USD_NET | PRECIO_PUBLICADO | https://networkdevicesinc.com/products/pan-pa-1410 |
| firewall_atp | ATP central 60 meses por miembro HA | 2 | 12825 USD_NET | PRECIO_PUBLICADO | https://networkdevicesinc.com/products/pan-pa-1410-atp-5yr |
| firewall_support | Soporte fabricante PA-1410, 60 meses | 2 | 10500 USD_NET | LISTA_USD_DE_CANAL | https://www.layer7.co.za/firewalls/pa-1400/pa-1410 |
| wan_ge | Distribuidor WAN MikroTik hEX E50UG, bridge VLAN | 45 | 77048 CLP_GROSS | PRECIO_FABRICANTE_CONVERSION_PLANIFICACION | https://mikrotik.com/product/hex_2024 |
| wan_mgig | Distribuidor WAN-A central MikroTik CRS310, bridge VLAN 2,5G | 1 | 281459 CLP_GROSS | PRECIO_FABRICANTE_CONVERSION_PLANIFICACION | https://mikrotik.com/product/crs310_8g_2s_in |
| cpe_5g | CPE móvil Entel 5G, comprado | 22 | 342850 CLP_GROSS | PRECIO_PUBLICADO | https://www.spdigital.cl/router-tp-link-archer-nx500-5g-ax3000-wi-fi-6-dual-band-467-gbps-5g-easymesh-y-plug-and-play/ |
| cpe_4g | CPE móvil WOM 4G, comprado | 22 | 158790 CLP_GROSS | PRECIO_PUBLICADO | https://www.spdigital.cl/4g-cat6-ac1200-wireless-dual-band-gigabit-router/ |
| ap | AP Wi-Fi de contingencia | 48 | 300000 CLP_GROSS | RESERVA_INGENIERIA | https://www.cisco.com/c/en/us/products/collateral/wireless/business-100-series-access-points/business-access-point-ds.html |
| pc_wifi | Reserva máxima Wi-Fi PCs existentes | 650 | 50000 CLP_GROSS | RESERVA_INGENIERIA | None |
| psu_600 | Segunda fuente switches 24P | 29 | 799 USD_NET | PRECIO_PUBLICADO | https://networkdevicesinc.com/products/pwr-c5-600wac |
| psu_1000 | Segunda fuente switches 48P | 17 | 2962.99 USD_NET | PRECIO_PUBLICADO_CONDICIONADO | https://www.cdw.com/product/cisco-config-5-power-supply-hot-plug-1000-watt/5400630 |
| fw_psu | Reserva segunda fuente firewall central | 2 | 900000 CLP_GROSS | RESERVA_INGENIERIA | None |
| lan_optics | Transceptores LAN central 10G | 8 | 300000 CLP_GROSS | RESERVA_INGENIERIA | None |
| fiber_patch | Latiguillo óptico central | 4 | 50000 CLP_GROSS | RESERVA_INGENIERIA | None |
| hsci | Cable HA2 HSCI central | 1 | 250000 CLP_GROSS | RESERVA_INGENIERIA | None |
| rack_patch | Cat6, organización y accesorios de montaje | 23 | 800000 CLP_GROSS | RESERVA_INGENIERIA | None |
| rf_survey | Diseño RF, instalación y aceptación Wi-Fi | 23 | 500000 CLP_GROSS | RESERVA_INGENIERIA | None |
| deployment | Implantación y migración de red por sede | 23 | 2500000 CLP_GROSS | RESERVA_INGENIERIA | None |
| regional_logistics | Traslados regionales y logística de implantación | 1 | 25000000 CLP_GROSS | RESERVA_INGENIERIA | None |
| central_engineering | Ingeniería común, laboratorio y documentación | 1 | 6550000 CLP_GROSS | RESERVA_INGENIERIA | None |
| ha_dc2_memory | DC-02: ampliación de 32 a 64 GiB RAM | 1 | 250000 CLP_GROSS | RESERVA_INGENIERIA | None |
| ha_dc2_storage | DC-02: par SSD empresarial 3,84 TB en espejo | 1 | 1200000 CLP_GROSS | RESERVA_INGENIERIA | None |


## Partidas y fuentes de la alternativa B

| ID | Partida | Cantidad | Precio de origen | Evidencia | Fuente |
|---|---|---|---|---|---|
| cpe_5g | CPE móvil Entel 5G, comprado | 22 |  CLP_GROSS | PRECIO_PUBLICADO | https://www.spdigital.cl/router-tp-link-archer-nx500-5g-ax3000-wi-fi-6-dual-band-467-gbps-5g-easymesh-y-plug-and-play/ |
| cpe_4g | CPE móvil WOM 4G, comprado | 22 |  CLP_GROSS | PRECIO_PUBLICADO | https://www.spdigital.cl/4g-cat6-ac1200-wireless-dual-band-gigabit-router/ |
| ap | AP Wi-Fi de contingencia | 48 |  CLP_GROSS | RESERVA_INGENIERIA | https://www.cisco.com/c/en/us/products/collateral/wireless/business-100-series-access-points/business-access-point-ds.html |
| pc_wifi | Reserva máxima Wi-Fi PCs existentes | 650 |  CLP_GROSS | RESERVA_INGENIERIA | None |
| lan_optics | Transceptores LAN central 10G | 8 |  CLP_GROSS | RESERVA_INGENIERIA | None |
| fiber_patch | Latiguillo óptico central | 4 |  CLP_GROSS | RESERVA_INGENIERIA | None |
| rack_patch | Cat6, organización y accesorios de montaje | 23 |  CLP_GROSS | RESERVA_INGENIERIA | None |
| rf_survey | Diseño RF, instalación y aceptación Wi-Fi | 23 |  CLP_GROSS | RESERVA_INGENIERIA | None |
| deployment | Implantación y migración de red por sede | 23 |  CLP_GROSS | RESERVA_INGENIERIA | None |
| regional_logistics | Traslados regionales y logística de implantación | 1 |  CLP_GROSS | RESERVA_INGENIERIA | None |
| central_engineering | Ingeniería común, laboratorio y documentación | 1 |  CLP_GROSS | RESERVA_INGENIERIA | None |
| ha_dc2_memory | DC-02: ampliación de 32 a 64 GiB RAM | 1 |  CLP_GROSS | RESERVA_INGENIERIA | None |
| ha_dc2_storage | DC-02: par SSD empresarial 3,84 TB en espejo | 1 |  CLP_GROSS | RESERVA_INGENIERIA | None |
| b_lacp_dac | DAC MikroTik XS+DA0001 1m · enlaces LACP interswitch | 44 | 37271 CLP_GROSS | PRECIO_FABRICANTE_USD_CONVERSION_PLANIFICACION | https://mikrotik.com/product/xs_da0001 |
| b_wan_hex | Distribuidor WAN MikroTik hEX E50UG · bridge VLAN | 45 | 77048 CLP_GROSS | PRECIO_FABRICANTE_USD_CONVERSION_PLANIFICACION | https://mikrotik.com/product/hex_2024 |
| b_wan_crs310 | Distribuidor WAN-A central MikroTik CRS310-8G+2S+IN | 1 | 281459 CLP_GROSS | PRECIO_FABRICANTE_USD_CONVERSION_PLANIFICACION | https://mikrotik.com/product/crs310_8g_2s_in |
| b_router_ccr2004 | Router estándar MikroTik CCR2004-16G-2S+ | 42 | 553350 CLP_GROSS | PRECIO_FABRICANTE_USD_CONVERSION_PLANIFICACION | https://mikrotik.com/product/ccr2004_16g_2splus |
| b_router_rb5009 | Router sede pequeña MikroTik RB5009UG+S+IN | 2 | 307466 CLP_GROSS | PRECIO_PUBLICADO_CHILE | https://www.redcetus.cl/shop/mikrotik-rb5009ug-s-in-router-home-lab-4962 |
| b_switch_crs328 | Switch PoE MikroTik CRS328-24P-4S+RM | 44 | 646990 CLP_GROSS | PRECIO_PUBLICADO_CHILE | https://www.tecnomas.cl/productos/categorias/Switches?pagina=13 |
| b_firewall_dec3852 | Appliance OPNsense DEC3852 | 2 | 2683741 CLP_GROSS | PRECIO_FABRICANTE_EUR_CONVERSION_PLANIFICACION | https://shop.opnsense.com/product/dec3852-opnsense-rack-security-appliance/ |

## Revisión WAN-2

A/B usan 45 hEX E50UG (USD 59,95) y un CRS310 (USD 219). Precios sugeridos consultados el 24-10-2026 en las páginas oficiales enlazadas. Se convierten con USD/CLP 1000, reserva importadora 8 % e IVA 19 %, redondeando el unitario bruto a CLP 77.048 y 281.459. Misma base A/B, sin doble IVA ni nueva reserva sobre estos unitarios. No constituyen contrato.
