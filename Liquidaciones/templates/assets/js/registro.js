async function nuevoEmpleado() {
  const form = document.getElementById("nuevo_empleado");
  const data = Object.fromEntries(new FormData(form).entries());

  // Normalizar numéricos
  if (data.empresa_id) data.empresa_id = Number(data.empresa_id);
  if (data.sueldo_base) data.sueldo_base = Number(data.sueldo_base);
  if (data.afp_id) data.afp_id = Number(data.afp_id);
  if (data.salud_id) data.salud_id = Number(data.salud_id);
  if (data.afc_id) data.afc_id = data.afc_id ? Number(data.afc_id) : null;

  try {
    const res = await fetch("/api/v1/empleados", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });
    if (!res.ok) {
      const err = await res.json().catch(() => ({}));
      alert("Error al crear empleado: " + (err.detail || res.status));
      return;
    }
    const json = await res.json();
    alert("Empleado creado con id: " + json.id);
    form.reset();
  } catch (e) {
    alert("Fallo de red.");
  }
}